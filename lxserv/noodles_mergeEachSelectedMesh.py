# python

import lx, modo, mc_noodles

"""A simple example of a blessed MODO command using the commander module.
https://github.com/adamohern/commander for details"""

class CommandClass(mc_noodles.CommanderClass):

    def commander_execute(self, msg, flags):
        meshes = modo.Scene().selectedByType('mesh')

        for mesh in meshes:

            lx.eval('item.create mesh {%s}' % (mesh.name + "_merge"))
            lx.eval('preset.do "[itemtypes]:MeshOperations/edit/pmodel.meshmerge.itemtype"')
            mesh_merge = modo.Scene().selected[0].id

            lx.eval('item.link pmodel.meshmerge.graph %s %s posT:0 replace:false' % (mesh.id, mesh_merge))
            mesh.channel('visible').set(2)

lx.bless(CommandClass, 'noodles.mergeEachSelectedMesh')
