import bpy

class MammothComponents(bpy.types.Panel):
	bl_label = 'Mammoth Components'
	bl_space_type = 'PROPERTIES'
	bl_region_type = 'WINDOW'
	bl_context = 'object'

	def draw(self, context):
		layout = self.layout
		obj = context.object
		
		row = layout.row()
		row.label('tits')