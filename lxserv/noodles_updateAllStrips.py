# python

import lx, modo, mc_noodles

"""A simple example of a blessed MODO command using the commander module.
https://github.com/adamohern/commander for details"""

class CommandClass(mc_noodles.CommanderClass):

    def commander_execute(self, msg, flags):
        saved_selection = modo.Scene().selected

        fusion_items = modo.Scene().items('sdf.item')

        for i in fusion_items:
            i.select(True)
            lx.eval('@StripMacro')

        lx.eval('select.drop item')
        for i in saved_selection:
            i.select()

        lx.eval('noodles.toggleStrips true')

lx.bless(CommandClass, 'noodles.updateAllStrips')
