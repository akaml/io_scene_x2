# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation, either version 3
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#  All rights reserved.
#
# ##### END GPL LICENSE BLOCK #####

# <pep8 compliant>

bl_info = {
    "name": "DirectX X Format",
    "author": "Bibindon",
    "version": (0, 0, 1),
    "blender": (2, 79, 0),
    "location": "File > Export > DirectX (.x)",
    "description": "For personally customizing and using, this addon was "
                   "forked from official DirectX X format exporter"
                   "(https://github.com/cdbfoster/io_scene_x).",
    "support": "TESTING",
    "category": "Import-Export"}

if "bpy" in locals():
    import imp
    imp.reload(export_x)
else:
    from . import export_x

import bpy
from bpy.props import BoolProperty
from bpy.props import EnumProperty
from bpy.props import StringProperty


class ExportDirectX2(bpy.types.Operator):
    """Export selection to DirectX"""

    bl_idname = "export_scene.x"
    bl_label = "Export DirectX"

    filepath = StringProperty(subtype='FILE_PATH')

    def execute(self, context):
        self.filepath = bpy.path.ensure_ext(self.filepath, ".x")

        Exporter = export_x.DirectXExporter(self, context)
        Exporter.Export()
        return {'FINISHED'}

    def invoke(self, context, event):
        if not self.filepath:
            self.filepath = bpy.path.ensure_ext(bpy.data.filepath, ".x")
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

class ExportDirectX2_Preferences(bpy.types.AddonPreferences):
    bl_idname = __name__

    # Export options

    SelectedOnly = BoolProperty(
        name="Export Selected Objects Only",
        description="Export only selected objects",
        default=True)

    CoordinateSystem = EnumProperty(
        name="Coordinate System",
        description="Use the selected coordinate system for export",
        items=(('LEFT_HANDED', "Left-Handed", "Use a Y up, Z forward system or a Z up, -Y forward system"),
               ('RIGHT_HANDED', "Right-Handed", "Use a Y up, -Z forward system or a Z up, Y forward system")),
        default='LEFT_HANDED')

    UpAxis = EnumProperty(
        name="Up Axis",
        description="The selected axis points upward",
        items=(('Y', "Y", "The Y axis points up"),
               ('Z', "Z", "The Z axis points up")),
        default='Y')

    ExportMeshes = BoolProperty(
        name="Export Meshes",
        description="Export mesh objects",
        default=True)

    ExportNormals = BoolProperty(
        name="    Export Normals",
        description="Export mesh normals",
        default=True)

    FlipNormals = BoolProperty(
        name="        Flip Normals",
        description="Flip mesh normals before export",
        default=False)

    ExportUVCoordinates = BoolProperty(
        name="    Export UV Coordinates",
        description="Export mesh UV coordinates, if any",
        default=True)

    ExportMaterials = BoolProperty(
        name="    Export Materials",
        description="Export material properties and reference image textures",
        default=True)

    ExportActiveImageMaterials = BoolProperty(
        name="        Reference Active Images as Textures",
        description="Reference the active image of each face as a texture, "\
            "as opposed to the image assigned to the material",
        default=False)

    ExportVertexColors = BoolProperty(
        name="    Export Vertex Colors",
        description="Export mesh vertex colors, if any",
        default=False)

    ExportSkinWeights = BoolProperty(
        name="    Export Skin Weights",
        description="Bind mesh vertices to armature bones",
        default=False)

    ApplyModifiers = BoolProperty(
        name="    Apply Modifiers",
        description="Apply the effects of object modifiers before export",
        default=False)

    ExportArmatureBones = BoolProperty(
        name="Export Armature Bones",
        description="Export armatures bones",
        default=False)

    ExportRestBone = BoolProperty(
        name="    Export Rest Position",
        description="Export bones in their rest position (recommended for "\
            "animation)",
        default=False)

    ExportAnimation = BoolProperty(
        name="Export Animations",
        description="Export object and bone animations.  Data is exported for "\
            "every frame",
        default=False)

    IncludeFrameRate = BoolProperty(
        name="    Include Frame Rate",
        description="Include the AnimTicksPerSecond template which is "\
            "used by some engines to control animation speed",
        default=False)

    ExportActionsAsSets = BoolProperty(
        name="    Export Actions as AnimationSets",
        description="Export each action of each object as a separate "\
            "AnimationSet. Otherwise all current actions are lumped "\
            "together into a single set",
        default=False)

    ExportNLATrackAction = BoolProperty(
        name="        Export NLA track Actions",
        description="Export NLA track actions",
        default=False)

    Verbose = BoolProperty(
        name="Verbose",
        description="Run the exporter in debug mode. Check the console for "\
            "output",
        default=False)

    def draw(self, context):
        layout = self.layout

        layout.prop(self, "SelectedOnly")
        layout.prop(self, "CoordinateSystem")
        layout.prop(self, "UpAxis")
        layout.prop(self, "ExportMeshes")
        layout.prop(self, "ExportNormals")
        layout.prop(self, "FlipNormals")
        layout.prop(self, "ExportUVCoordinates")
        layout.prop(self, "ExportMaterials")
        layout.prop(self, "ExportActiveImageMaterials")
        layout.prop(self, "ExportVertexColors")
        layout.prop(self, "ExportSkinWeights")
        layout.prop(self, "ApplyModifiers")
        layout.prop(self, "ExportArmatureBones")
        layout.prop(self, "ExportRestBone")
        layout.prop(self, "ExportAnimation")
        layout.prop(self, "IncludeFrameRate")
        layout.prop(self, "ExportActionsAsSets")
        layout.prop(self, "ExportNLATrackAction")
        layout.prop(self, "Verbose")


def menu_func(self, context):
    self.layout.operator(ExportDirectX2.bl_idname, text="DirectX (.x)")


def register():
    bpy.utils.register_module(__name__)

    bpy.types.INFO_MT_file_export.append(menu_func)


def unregister():
    bpy.utils.unregister_module(__name__)

    bpy.types.INFO_MT_file_export.remove(menu_func)


if __name__ == "__main__":
    register()
