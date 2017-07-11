# python

import modo

restore_sel = modo.Scene().selected
has_error = False

for i in modo.Scene().items('sdf.item'):
    if not i.channel('visible').get():
        continue

    restore = i.channel('OutputMeshMode').get()

    i.channel('OutputMeshMode').set('outModeFinal')

    i.select(True)
    try:
        # lx.eval('!!@MeshOut.pl 0')
        # lx.eval('item.tag string FDup 123')
        lx.eval('item.duplicate instance:false type:sdf.item all:false mods:true')
        lx.eval('item.setType mesh locator')
    except:
        has_error = True

    i.channel('FusionOn').set(False)

    i.channel('OutputMeshMode').set(restore)

lx.eval('select.drop item')
for i in restore_sel:
    i.select()

if has_error:
    modo.dialogs.alert("Something went wrong.", "At least one Fusion item failed to convert to Mesh. Just so ya' know.")
