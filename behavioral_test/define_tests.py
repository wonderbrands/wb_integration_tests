from odoo import models, fields, api
from behave.runner import Runner, Context
from behave.configuration import Configuration
import os
import logging

_logger = logging.getLogger(__name__)

"""
class DefineTestsWhenInstall(models.Model, Runner):
    _inherit = "ir.module.module"
 
    def _list_subpaths(self):
        _logger.info("DefineTestsWhenInstall._import_subpaths")
        curretn_path = os.path.dirname(os.path.abspath(__file__))
        _logger.info(curretn_path)
        _logger.info("Get directories in current path")
        dirs = os.listdir(curretn_path)
        _logger.info(dirs)
        return dirs

    def run(self):
        self.context.odoo_env = self.env
        return super().run()


    def button_install(self):
        _logger.info("DefineTestsWhenInstall.button_install")
        super().button_install()
        config = Configuration(["features/"])
        config.paths.append("features/math/steps/")
        config.paths.append("features/string/steps/")

        runner = Runner(config)
        runner.run()
"""

#the upper code is the right way
#this is just for testing withouit the need of install a module

class CustomRunner(Runner):
    def run(self, odoo_env):
        self.context = Context(self)
        _logger.info("CustomRunner.run")
        _logger.info(self.context)
        self.context.odoo_env = odoo_env
        _logger.info("CustomRunner.run")
        _logger.info(self.context.odoo_env)
        return super().run()

class DefineTestsWhenInstall(models.BaseModel):
    _inherit = "base"
    def _list_subpaths(self):
        _logger.info("DefineTestsWhenInstall._import_subpaths")
        curretn_path = os.path.dirname(os.path.abspath(__file__))
        _logger.info(curretn_path)
        _logger.info("Get directories in current path")
        dirs = [os.path.abspath(os.path.join(curretn_path, d)) for d in os.listdir(curretn_path) if os.path.isdir(os.path.join(curretn_path, d)) and d != "__pycache__"]
        _logger.info(dirs)
        return dirs

    def run(self):
        """
        self.context.odoo_env = self.env
        _logger.info("DefineTestsWhenInstall.run")
        config = Configuration(self._list_subpaths())
        _logger.info(config.paths)
        runner = Runner(config)
        _logger.info(runner)
        runner.run()
        """
        _logger.info("DefineTestsWhenInstall.run")
        config = Configuration(self._list_subpaths())
        _logger.info(config.paths)
        runner = CustomRunner(config)
        _logger.info(runner)
        runner.run(self.env)

    def write(self, values):
        _logger.info("DefineTestsWhenInstall.write")
        record = super().write(values)
        _logger.info(record)
        self.run()
        return record