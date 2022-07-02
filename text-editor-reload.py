# ***** BEGIN GPL LICENSE BLOCK *****
#
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ***** END GPL LICENCE BLOCK *****

bl_addon_info = {
    "name": "Reload if Modified",
    "author": "Dany Lebel (Axon_D)",
    "version": (1,0),
    "blender": (3, 2, 0),
    "location": "Text Editor -> Header Bar -> Reload if Modified",
    "description": "Determine if a text datablock must be reloaded from file in the case that it has changed",
    "warning": "",
    "wiki_url": "http://wiki.blender.org/index.php/Extensions:2.5/Py/Scripts/Text_Editor/Reload_if_Modified",
    "tracker_url": "http://projects.blender.org/tracker/index.php?func=detail&aid=25277&group_id=153&atid=467",
    "category": "Text Editor"}

"""
This addon will automatically reload a text datablock if its source file
does not corresponds to the last blendfile version. This must be checked
for each file wanted to be updated automatically. It has no effect on internal datablock. 
"""

import bpy


def reload_if_modified(self, context):
    text = bpy.context.space_data.text
    
    if hasattr(text, 'reload_if_modified'):
        text = bpy.context.space_data.text

        if text.is_in_memory:
            text.reload_if_modified = False
            return None
        
        else :
            layout = self.layout
            row = layout.row()
            row.prop(text, "reload_if_modified")
            
            if text.is_modified and text.reload_if_modified:
                bpy.ops.text.reload()

        


def register():
    bpy.types.Text.reload_if_modified : bpy.props.BoolProperty(
                            name='Reload if Modified',
                            description=
                            'Automatically reload text file if it has changed',
                            default=False)
    #bpy.types.TEXT_PT_properties.append(reload_if_modified)
    bpy.types.TEXT_HT_header.append(reload_if_modified)


def unregister():
    if hasattr(bpy.types.Text, 'reload_if_modified'):
        del bpy.types.Text.reload_if_modified
    #bpy.types.TEXT_PT_properties.remove(reload_if_modified)
    bpy.types.TEXT_HT_header.remove(reload_if_modified)


if __name__ == '__main__':
    register()
