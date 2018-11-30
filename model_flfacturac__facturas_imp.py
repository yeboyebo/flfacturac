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

    def initValidation(name, data=None):
        return form.iface.initValidation(name, data)

    def iniciaValoresLabel(self, template=None, cursor=None, data=None):
        return form.iface.iniciaValoresLabel(self, template, cursor)

    def bChLabel(fN=None, cursor=None):
        return form.iface.bChLabel(fN, cursor)

    def getFilters(self, name, template=None):
        return form.iface.getFilters(self, name, template)

    def getForeignFields(self, template=None):
        return form.iface.getForeignFields(self, template)

    def getDesc():
        return form.iface.getDesc()


# @class_declaration facturas_imp #
class facturas_imp(flfacturac_facturas_imp, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


definitions = importlib.import_module("models.flfacturac.facturas_imp_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
