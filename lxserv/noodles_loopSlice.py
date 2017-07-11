# python
# Made with Replay
# mechanicalcolor.com

import lx, modo, mc_noodles

"""A simple example of a blessed MODO command using the commander module.
https://github.com/adamohern/commander for details"""

class CommandClass(mc_noodles.CommanderClass):

    def commander_arguments(self):
        return [
            {
                'name': 'loops',
                'datatype': 'integer'
            }
        ]

    def commander_execute(self, msg, flags):
        loops = not self.commander_arg_value(0)

        lx.eval('@noodles_loopSliceAuto.py %s' % loops)

lx.bless(CommandClass, 'noodles.loopSlice')
