# @class_declaration interna_facturas_imp #
import importlib

from YBUTILS.viewREST import helpers

from models.flfacturac import models as modelos


class interna_facturas_imp(modelos.mtd_facturas_imp, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfacturac_facturas_imp #
class flfacturac_facturas_imp(interna_facturas_imp, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration facturas_imp #
class facturas_imp(flfacturac_facturas_imp, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfacturac.facturas_imp_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
