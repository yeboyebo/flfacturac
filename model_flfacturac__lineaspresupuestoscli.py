# @class_declaration interna_lineaspresupuestoscli #
import importlib

from YBUTILS.viewREST import helpers

from models.flfacturac import models as modelos


class interna_lineaspresupuestoscli(modelos.mtd_lineaspresupuestoscli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfacturac_lineaspresupuestoscli #
class flfacturac_lineaspresupuestoscli(interna_lineaspresupuestoscli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration lineaspresupuestoscli #
class lineaspresupuestoscli(flfacturac_lineaspresupuestoscli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfacturac.lineaspresupuestoscli_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
