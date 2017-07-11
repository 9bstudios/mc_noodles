# python

loops = lx.args()[0]

lx.eval('tool.set poly.loopSlice on')
lx.eval('tool.flag poly.loopSlice auto false')
lx.eval('tool.attr poly.loopSlice count %s' % loops)
lx.eval('tool.doApply')
lx.eval('tool.set poly.loopSlice off')
