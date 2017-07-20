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

    def cmd_Flags(self):
        # This is the key to this command.
        # It send the commands as if not called from an external command.
        # And thus the tool is not refired as a new instance.
        return lx.symbol.fCMD_QUIET

    def commander_execute(self, msg, flags):
        loops = self.commander_arg_value(0)

        if lx.eval1('tool.set poly.loopSlice ?') == 'on':
            lx.eval('tool.set poly.loopSlice off')

        lx.eval('tool.set poly.loopSlice on')
        lx.eval('tool.flag poly.loopSlice auto false')
        lx.eval('tool.attr poly.loopSlice count %s' % loops)
        lx.eval('tool.doApply')
        lx.eval('tool.set poly.loopSlice off')

lx.bless(CommandClass, 'noodles.loopSlice')
