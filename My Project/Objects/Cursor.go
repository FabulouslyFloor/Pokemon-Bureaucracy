components {
  id: "cursor"
  component: "/Scripts/cursor.script"
}
components {
  id: "replace_mouse_cursor"
  component: "/Scripts/replace_mouse_cursor.script"
}
embedded_components {
  id: "collisionobject"
  type: "collisionobject"
  data: "type: COLLISION_OBJECT_TYPE_KINEMATIC\n"
  "mass: 0.0\n"
  "friction: 0.1\n"
  "restitution: 0.5\n"
  "group: \"Cursor\"\n"
  "mask: \"draggable\"\n"
  "embedded_collision_shape {\n"
  "  shapes {\n"
  "    shape_type: TYPE_SPHERE\n"
  "    position {\n"
  "      x: -4.0\n"
  "      y: 4.0\n"
  "    }\n"
  "    rotation {\n"
  "    }\n"
  "    index: 0\n"
  "    count: 1\n"
  "  }\n"
  "  data: 20.0\n"
  "}\n"
  ""
}
embedded_components {
  id: "sprite"
  type: "sprite"
  data: "default_animation: \"simple-hand-cursor-free-png\"\n"
  "material: \"/builtins/materials/sprite.material\"\n"
  "textures {\n"
  "  sampler: \"texture_sampler\"\n"
  "  texture: \"/Test Images/Testing.atlas\"\n"
  "}\n"
  ""
  position {
    z: 1.0
  }
  scale {
    x: 0.05
    y: 0.05
  }
}
