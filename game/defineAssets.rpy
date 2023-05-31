init python:
    from os import path

    def define_assets(asset_folder):
        for file in renpy.list_files():
            if asset_folder in file:
                file_name = path.splitext(path.basename(file))[0]
                if file.endswith((".png", ".jpg")):
                    renpy.image(file_name, file)
                elif file.endswith((".wav", ".mp2", ".mp3", ".ogg", ".opus", ".webm", ".flv", ".vob")):
                    globals()[file_name] = file
            # if mod_folder in file:
            #     file_name = path.splitext(path.basename(file))[0]

            #     if file.endswith((".png", ".jpg")):
            #         if sprites_folder and '%s/%s' % (mod_folder, sprites_folder) in file:
            #                 renpy.image(
            #                     file_name,
            #                     ConditionSwitch(
            #                         "persistent.sprite_time == 'sunset'",
            #                         im.MatrixColor(
            #                             file,
            #                             im.matrix.tint(0.94, 0.82, 1.0)
            #                         ),
            #                         "persistent.sprite_time == 'night'",
            #                         im.MatrixColor(
            #                             file,
            #                             im.matrix.tint(0.63, 0.78, 0.82)
            #                         ),
            #                         "True", file
            #                     )
            #                 )
            #         else:
            #             renpy.image(file_name, file)
            #     elif file.endswith((".wav", ".mp2", ".mp3", ".ogg", ".opus", ".webm", ".flv", ".vob")):
            #         globals()[file_name] = file
