# @class_declaration interna_huecos #
import importlib

from YBUTILS.viewREST import helpers

from models.flfacturac import models as modelos


class interna_huecos(modelos.mtd_huecos, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfacturac_huecos #
class flfacturac_huecos(interna_huecos, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration huecos #
class huecos(flfacturac_huecos, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfacturac.huecos_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
