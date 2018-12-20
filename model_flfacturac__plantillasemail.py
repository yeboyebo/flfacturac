# @class_declaration interna_plantillasemail #
import importlib

from YBUTILS.viewREST import helpers

from models.flfacturac import models as modelos


class interna_plantillasemail(modelos.mtd_plantillasemail, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfacturac_plantillasemail #
class flfacturac_plantillasemail(interna_plantillasemail, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration plantillasemail #
class plantillasemail(flfacturac_plantillasemail, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfacturac.plantillasemail_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
