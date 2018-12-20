# @class_declaration interna_facturascli #
import importlib

from YBUTILS.viewREST import helpers

from models.flfacturac import models as modelos


class interna_facturascli(modelos.mtd_facturascli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfacturac_facturascli #
class flfacturac_facturascli(interna_facturascli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration facturascli #
class facturascli(flfacturac_facturascli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfacturac.facturascli_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
