components {
  id: "PassportFill"
  component: "/Scripts/PassportFill.script"
}
embedded_components {
  id: "sprite"
  type: "sprite"
  data: "default_animation: \"TestingPassportLarge\"\n"
  "material: \"/builtins/materials/sprite.material\"\n"
  "textures {\n"
  "  sampler: \"texture_sampler\"\n"
  "  texture: \"/Test Images/Testing.atlas\"\n"
  "}\n"
  ""
  scale {
    x: 0.5
    y: 0.5
  }
}
embedded_components {
  id: "PokemonSprite1"
  type: "factory"
  data: "prototype: \"/Objects/PokemonSprites/Sprites1.go\"\n"
  "dynamic_prototype: true\n"
  ""
}
embedded_components {
  id: "PokemonSprite2"
  type: "factory"
  data: "prototype: \"/Objects/PokemonSprites/Sprites2.go\"\n"
  ""
}
embedded_components {
  id: "PokemonSprite3"
  type: "factory"
  data: "prototype: \"/Objects/PokemonSprites/Sprites3.go\"\n"
  ""
}
embedded_components {
  id: "PokemonSprite4"
  type: "factory"
  data: "prototype: \"/Objects/PokemonSprites/Sprites4.go\"\n"
  ""
}
embedded_components {
  id: "PokemonSprite5"
  type: "factory"
  data: "prototype: \"/Objects/PokemonSprites/Sprites5.go\"\n"
  ""
}
embedded_components {
  id: "PokemonSprite6"
  type: "factory"
  data: "prototype: \"/Objects/PokemonSprites/Sprites6.go\"\n"
  ""
}
embedded_components {
  id: "PokemonSprite7"
  type: "factory"
  data: "prototype: \"/Objects/PokemonSprites/Sprites7.go\"\n"
  ""
}
embedded_components {
  id: "PokemonSprite8"
  type: "factory"
  data: "prototype: \"/Objects/PokemonSprites/Sprites8.go\"\n"
  ""
}
embedded_components {
  id: "PokemonSprite9"
  type: "factory"
  data: "prototype: \"/Objects/PokemonSprites/Sprites9.go\"\n"
  ""
}
embedded_components {
  id: "PokemonSprite10"
  type: "factory"
  data: "prototype: \"/Objects/PokemonSprites/Sprites10.go\"\n"
  ""
}
embedded_components {
  id: "PokemonSprite11"
  type: "factory"
  data: "prototype: \"/Objects/PokemonSprites/Sprites11.go\"\n"
  ""
}
embedded_components {
  id: "PokemonSprite12"
  type: "factory"
  data: "prototype: \"/Objects/PokemonSprites/Sprites12.go\"\n"
  ""
}
embedded_components {
  id: "PokemonSprite13"
  type: "factory"
  data: "prototype: \"/Objects/PokemonSprites/Sprites13.go\"\n"
  ""
}
embedded_components {
  id: "PokemonSprite14"
  type: "factory"
  data: "prototype: \"/Objects/PokemonSprites/Sprites14.go\"\n"
  ""
}
embedded_components {
  id: "PokemonSprite15"
  type: "factory"
  data: "prototype: \"/Objects/PokemonSprites/Sprites15.go\"\n"
  ""
}
embedded_components {
  id: "PokemonSprite16"
  type: "factory"
  data: "prototype: \"/Objects/PokemonSprites/Sprites16.go\"\n"
  ""
}
embedded_components {
  id: "PokemonSprite17"
  type: "factory"
  data: "prototype: \"/Objects/PokemonSprites/Sprites17.go\"\n"
  ""
}
embedded_components {
  id: "PokemonSprite18"
  type: "factory"
  data: "prototype: \"/Objects/PokemonSprites/Sprites18.go\"\n"
  ""
}
embedded_components {
  id: "PokemonSprite19"
  type: "factory"
  data: "prototype: \"/Objects/PokemonSprites/Sprites19.go\"\n"
  ""
}
embedded_components {
  id: "PokemonSprite20"
  type: "factory"
  data: "prototype: \"/Objects/PokemonSprites/Sprites20.go\"\n"
  ""
}
embedded_components {
  id: "PokemonSprite21"
  type: "factory"
  data: "prototype: \"/Objects/PokemonSprites/Sprites21.go\"\n"
  ""
}
embedded_components {
  id: "collisionobject"
  type: "collisionobject"
  data: "type: COLLISION_OBJECT_TYPE_KINEMATIC\n"
  "mass: 0.0\n"
  "friction: 0.1\n"
  "restitution: 0.5\n"
  "group: \"draggable\"\n"
  "mask: \"Cursor\"\n"
  "embedded_collision_shape {\n"
  "  shapes {\n"
  "    shape_type: TYPE_BOX\n"
  "    position {\n"
  "    }\n"
  "    rotation {\n"
  "    }\n"
  "    index: 0\n"
  "    count: 3\n"
  "  }\n"
  "  data: 205.0\n"
  "  data: 134.0\n"
  "  data: 10.0\n"
  "}\n"
  ""
}
embedded_components {
  id: "Name"
  type: "label"
  data: "size {\n"
  "  x: 128.0\n"
  "  y: 32.0\n"
  "}\n"
  "color {\n"
  "  x: 0.0\n"
  "  y: 0.0\n"
  "  z: 0.0\n"
  "}\n"
  "pivot: PIVOT_W\n"
  "text: \"Label\"\n"
  "font: \"/Fonts/PokemonBodyHeavy.font\"\n"
  "material: \"/builtins/fonts/label-df.material\"\n"
  ""
  position {
    y: 100.0
  }
}
embedded_components {
  id: "Type1"
  type: "label"
  data: "size {\n"
  "  x: 128.0\n"
  "  y: 32.0\n"
  "}\n"
  "color {\n"
  "  x: 0.0\n"
  "  y: 0.0\n"
  "  z: 0.0\n"
  "}\n"
  "pivot: PIVOT_W\n"
  "text: \"Label\"\n"
  "font: \"/Fonts/PokemonBodyHeavy.font\"\n"
  "material: \"/builtins/fonts/label-df.material\"\n"
  ""
  position {
    x: 10.0
    y: 60.0
  }
}
embedded_components {
  id: "Type2"
  type: "label"
  data: "size {\n"
  "  x: 128.0\n"
  "  y: 32.0\n"
  "}\n"
  "color {\n"
  "  x: 0.0\n"
  "  y: 0.0\n"
  "  z: 0.0\n"
  "}\n"
  "pivot: PIVOT_W\n"
  "text: \"Label\"\n"
  "font: \"/Fonts/PokemonBodyHeavy.font\"\n"
  "material: \"/builtins/fonts/label-df.material\"\n"
  ""
  position {
    x: 10.0
    y: 25.0
  }
}
embedded_components {
  id: "Ability"
  type: "label"
  data: "size {\n"
  "  x: 128.0\n"
  "  y: 32.0\n"
  "}\n"
  "color {\n"
  "  x: 0.0\n"
  "  y: 0.0\n"
  "  z: 0.0\n"
  "}\n"
  "pivot: PIVOT_W\n"
  "text: \"Label\"\n"
  "font: \"/Fonts/PokemonBodyHeavy.font\"\n"
  "material: \"/builtins/fonts/label-df.material\"\n"
  ""
  position {
    x: -115.0
    y: -10.0
  }
}
embedded_components {
  id: "Height"
  type: "label"
  data: "size {\n"
  "  x: 128.0\n"
  "  y: 32.0\n"
  "}\n"
  "color {\n"
  "  x: 0.0\n"
  "  y: 0.0\n"
  "  z: 0.0\n"
  "}\n"
  "pivot: PIVOT_W\n"
  "text: \"Label\"\n"
  "font: \"/Fonts/PokemonBodyHeavy.font\"\n"
  "material: \"/builtins/fonts/label-df.material\"\n"
  ""
  position {
    x: -110.0
    y: -45.0
  }
}
embedded_components {
  id: "Weight"
  type: "label"
  data: "size {\n"
  "  x: 128.0\n"
  "  y: 32.0\n"
  "}\n"
  "color {\n"
  "  x: 0.0\n"
  "  y: 0.0\n"
  "  z: 0.0\n"
  "}\n"
  "pivot: PIVOT_W\n"
  "text: \"Label\"\n"
  "font: \"/Fonts/PokemonBodyHeavy.font\"\n"
  "material: \"/builtins/fonts/label-df.material\"\n"
  ""
  position {
    x: -105.0
    y: -80.0
  }
}
embedded_components {
  id: "Gender"
  type: "label"
  data: "size {\n"
  "  x: 128.0\n"
  "  y: 32.0\n"
  "}\n"
  "color {\n"
  "  x: 0.0\n"
  "  y: 0.0\n"
  "  z: 0.0\n"
  "}\n"
  "pivot: PIVOT_W\n"
  "text: \"Label\"\n"
  "font: \"/Fonts/PokemonBodyHeavy.font\"\n"
  "material: \"/builtins/fonts/label-df.material\"\n"
  ""
  position {
    x: -105.0
    y: -110.0
  }
}
embedded_components {
  id: "Move1"
  type: "label"
  data: "size {\n"
  "  x: 128.0\n"
  "  y: 32.0\n"
  "}\n"
  "color {\n"
  "  x: 0.0\n"
  "  y: 0.0\n"
  "  z: 0.0\n"
  "}\n"
  "text: \"Label\"\n"
  "font: \"/Fonts/PokemonBodyHeavy.font\"\n"
  "material: \"/builtins/fonts/label-df.material\"\n"
  ""
  position {
    x: 100.0
    y: -40.0
  }
}
embedded_components {
  id: "Move2"
  type: "label"
  data: "size {\n"
  "  x: 128.0\n"
  "  y: 32.0\n"
  "}\n"
  "color {\n"
  "  x: 0.0\n"
  "  y: 0.0\n"
  "  z: 0.0\n"
  "}\n"
  "text: \"Label\"\n"
  "font: \"/Fonts/PokemonBodyHeavy.font\"\n"
  "material: \"/builtins/fonts/label-df.material\"\n"
  ""
  position {
    x: 100.0
    y: -80.0
  }
}
