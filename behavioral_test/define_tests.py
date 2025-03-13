import logging
from io import StringIO
import sys
from behave.runner import Runner, Context
from behave.configuration import Configuration
from odoo import models, api
import os
from behave.runner_util import parse_features
from behave.formatter._registry import make_formatters

_logger = logging.getLogger(__name__)

class OdooLogHandler(logging.Handler):
    """Custom log handler to redirect behave logs to Odoo logger"""
    def emit(self, record):
        formatted_message = self.format(record)
        _logger.info(f"BEHAVE: {formatted_message}")

class CustomRunner(Runner):
    def run_with_paths(self, odoo_env):
        with self.path_manager:
            self.setup_paths()
            _logger.info("CustomRunner.run - Initializing Context")
            
            # Make sure we're not creating a new context if one already exists
            self.context = Context(self)
            
            # Set the odoo_env on the context
            self.context.odoo_env = odoo_env
            _logger.info(f"Odoo Environment set on context: {odoo_env}")
            
            # Add a custom object to the context
            self.context.myobj = {"key": "value"}  # Replace with your custom object
            _logger.info(f"Added myobj to context: {self.context.myobj}")
            
            # Configure behave logging to redirect to Odoo
            behave_logger = logging.getLogger('behave')
            behave_logger.setLevel(logging.INFO)
            
            # Remove any existing handlers to avoid duplicates
            for handler in behave_logger.handlers[:]:
                behave_logger.removeHandler(handler)
                
            # Add our custom handler
            odoo_handler = OdooLogHandler()
            behave_logger.addHandler(odoo_handler)
            
            # Patch the print function to log to Odoo as well
            original_print = print
            
            def odoo_print(*args, **kwargs):
                # Call the original print
                original_print(*args, **kwargs)
                
                # Also log to Odoo
                message = " ".join(str(arg) for arg in args)
                _logger.info(f"BEHAVE PRINT: {message}")
                
            # Replace print globally during test run
            import builtins
            builtins.print = odoo_print
            
            try:            
                self.load_hooks()
                self.load_step_definitions()

                # -- ENSURE: context.execute_steps() works in weird cases (hooks, ...)
                # self.setup_capture()
                # self.run_hook("before_all", self.context)

                # -- STEP: Parse all feature files (by using their file location).
                feature_locations = [filename for filename in self.feature_locations()
                                    if not self.config.exclude(filename)]
                features = parse_features(feature_locations, language=self.config.lang)
                self.features.extend(features)

                # -- STEP: Run all features.
                stream_openers = self.config.outputs
                self.formatters = make_formatters(self.config, stream_openers)
                return self.run_model()
            finally:
                # Restore original print function
                builtins.print = original_print

class DefineTestsWhenInstall(models.AbstractModel):
    _inherit = "ir.module.module"  # ✅ Correct parent model

    def _list_subpaths(self):
        """Return the absolute path of the upper directory concatenated with 'features'"""
        _logger.info("DefineTestsWhenInstall._list_subpaths")
        current_path = os.path.dirname(os.path.abspath(__file__))
        _logger.info(f"Current Path: {current_path}")
        features_path = os.path.abspath(os.path.join(current_path, "..", "features"))
        _logger.info(f"Features Path: {features_path}")

        return [features_path]

    def run(self):
        """Runs the Behave tests"""
        _logger.info("DefineTestsWhenInstall.run - Starting Tests")

        try:
            # Configure Behave
            config = Configuration(["--format=pretty"])
            config.paths = self._list_subpaths()  # Add feature paths
            config.color = True  # Enable colored output

            _logger.info(f"Test Paths: {config.paths}")
            _logger.info(f"Test Format: {config.format}")

            # Run Behave tests
            runner = CustomRunner(config)
            _logger.info("Runner initialized")
            runner.run_with_paths(self.env)  # ✅ Pass Odoo Environment
        except Exception as e:
            _logger.error(f"❌ Error running Behave tests: {e}")

    def button_immediate_install(self):
        """Override button_immediate_install to run tests after installation"""
        _logger.info("DefineTestsWhenInstall.button_immediate_install - Triggered")

        try:
            record = super().button_immediate_install()  # ✅ Install module
            _logger.info("✅ Module installed successfully")

            self.run()  # ✅ Run Behave tests
        except Exception as e:
            _logger.error(f"❌ Error installing module: {e}")

        return record
