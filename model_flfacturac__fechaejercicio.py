# @class_declaration interna_fechaejercicio #
import importlib

from YBUTILS.viewREST import helpers

from models.flfacturac import models as modelos


class interna_fechaejercicio(modelos.mtd_fechaejercicio, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfacturac_fechaejercicio #
class flfacturac_fechaejercicio(interna_fechaejercicio, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration fechaejercicio #
class fechaejercicio(flfacturac_fechaejercicio, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfacturac.fechaejercicio_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
