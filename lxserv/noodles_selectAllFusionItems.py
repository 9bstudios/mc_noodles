# python

import lx, modo, mc_noodles

"""A simple example of a blessed MODO command using the commander module.
https://github.com/adamohern/commander for details"""

class CommandClass(mc_noodles.CommanderClass):

    def commander_execute(self, msg, flags):
        fusion_items = modo.Scene().items('sdf.item')

        for i in fusion_items:
            i.select()
            lx.eval('itemList.find')

lx.bless(CommandClass, 'noodles.selectAllFusionItems')
