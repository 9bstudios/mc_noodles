# python

import lx, modo, mc_noodles

"""A simple example of a blessed MODO command using the commander module.
https://github.com/adamohern/commander for details"""

class CommandClass(mc_noodles.CommanderClass):

    def commander_arguments(self):
        return [
            {
                'name': 'mode',
                'datatype': 'boolean',
                'flags': ['query', 'optional']
            }
        ]

    def commander_execute(self, msg, flags):
        mode = self.commander_arg_value(0)

        fusion_items = modo.Scene().items('sdf.item')

        if mode is None:
            mode = True
            for i in fusion_items:
                if i.channel('FusionOn').get():
                    mode = False
                    break

        for i in fusion_items:
            i.channel('FusionOn').set(mode)

    def commander_query(self, index):
        strip_items = modo.Scene().items('sdf.item')
        for i in strip_items:
            if i.channel('FusionOn').get():
                return False
        return True

lx.bless(CommandClass, 'noodles.toggleFusion')
