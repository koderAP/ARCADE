def render_story(dialog_box):
    story = (
        "Once upon a time, in a land far away,\n"
        "there lived a brave knight named Sir Lancelot.\n"
        "He embarked on a quest to rescue the princess,\n"
        "who was held captive by a fierce dragon."
    )

    # Split the story into separate lines
    story_lines = story.split('\n')
    
    # Add each line to the dialog_box
    for line in story_lines:
        dialog_box.text += line + '\n'
