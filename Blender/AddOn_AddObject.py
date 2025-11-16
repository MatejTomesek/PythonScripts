#add my custom script as addon

import bpy

class TestPanel(bpy.types.Panel):
    bl_label = "Test Panel"
    bl_idname = "PT_TestPanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Tool"
    bl_category = "My 1st Addon"
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.label(text= "Add an object", icon="CUBE")
        row = layout.row()
        row.operator("mesh.primitive_cube_add", icon="CUBE")
        row = layout.row()
        row.operator("mesh.primitive_uv_sphere_add", icon="SPHERE")

        
def register():
    bpy.utils.register_class(TestPanel)
    
def unregister():
    bpy.utils.register_class(TestPanel)
    
if __name__ == "__main__":
    register()