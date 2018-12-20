# @class_declaration interna_pedidosprov #
import importlib

from YBUTILS.viewREST import helpers

from models.flfacturac import models as modelos


class interna_pedidosprov(modelos.mtd_pedidosprov, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfacturac_pedidosprov #
class flfacturac_pedidosprov(interna_pedidosprov, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration pedidosprov #
class pedidosprov(flfacturac_pedidosprov, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfacturac.pedidosprov_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
