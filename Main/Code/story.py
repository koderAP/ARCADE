def render_story(dialog_box):
    story = (
        "Once upon a time, in a land far away,\n"
        "there lived a brave knight named Sir Lancelot.\n"
        "He embarked on a quest to rescue the princess,\n"
        "who was held captive by a fierce dragon."
    )

    story_lines = story.split('\n')
    
    for line in story_lines:
        dialog_box.text += line + '\n'

main_dialog = [
            "Greetings,     young     traveler!",
            "Welcome    to      the     icy     regions     of      Eldoria.\n\nI    am      the     Elder     guardian    of      this    land.",
            "I      sense     a     brave       spirit      within    you,      eager     to    explore     and     learn.\n\nAre    you     ready   to      embark      on      a   journey     of      discovery?",
            "While      the      icy      terrain      holds      its      own      mysteries,\n\nthere      is      much      more      to      explore      beyond      these      frosty      lands.",
            "Seek      out      the      warmth      of      the      desert      sands,\n\nwhere      a      wise      Elder      Frog      awaits.",
            "Their      knowledge      may      hold      the      key      to      \n\nunlocking      new      adventures      and      challenges.",
            "Venture      forth,      young      adventurer,\n\nand      may      the      winds      of      destiny      guide      your      path!"
        ]

sand_frog_dialog = [
            "Ah,      young      traveler,      you      have      found      your      way      to      the      sands      \n\nof      our      realm.",
            "Welcome!      Here,      amidst      the      swirling      dunes,      \n\nwisdom      awaits      those      who      seek      it.",

            "In      the      vast      expanse      of      this      desert,      \n\ndanger      lurks      in      the      form      of      rocky      obstacles.",
            "But      fear      not,      for      with      courage      and      swift      reflexes,      \n\nyou      can      navigate      this      terrain.",

            "Listen      closely,      young      one.      Board      the      landspeeder,      \n\nand      venture      forth      into      the      sandy      wilderness.",
            "Steer      clear      of      the      treacherous      rocks      that      dot      the      landscape,      \n\nand      your      journey      shall      be      a      fruitful      one.",

            "May      the      Force      be      with      you."

        ]


forest_frog_dialog = [
            "Greetings,      traveler.      If      it's      shelter      you      seek,      \n\nour      old      home      lies      just      beyond      these      ancient      trees.",

            "Nestled      within      this      forsaken      forest,      \nour      once      vibrant      abode      now      stands      silent      and      still.",
            "But      within      its      walls      lies      a      secret,      \na      game      of      challenges      and      puzzles      awaiting      discovery.",

            "The      path      to      our      dwelling      may      be      obscured      by      nature's      grasp,      but      fear      not.      Follow      the      overgrown      trail,      and      soon      you      shall      stand      before      the      entrance      to      our      humble      sanctuary.",

            "As      you      step      through      the      threshold,      prepare      yourself      for      a      descent      into      the      unknown.      The      floors      below      hold      the      keys      to      unlocking      the      mysteries      of      our      past.",

            "The      house      you      seek      was      once      the      home      of      an      old      man      who      cherished      his      collection      of      miniature      frogs.      Many      tales      were      told      of      their      playful      antics      and      the      hidden      wonders      within      these      walls.",

            "But      beware,      for      the      journey      ahead      is      not      for      the      faint      of      heart.      Only      those      with      resolve      and      wit      shall      prevail      in      the      face      of      adversity.",

            "So      venture      forth,      intrepid      traveler,      and      may      the      echoes      of      our      tales      guide      your      steps      through      the      shadows      of      our      forsaken      home."

        ]

forest_blob_dialog = [
            "Greetings,      traveler.      If      it's      shelter      you      seek,      \n\nour      old      home      lies      just      beyond      these      ancient      trees.",
            "Nestled      within      this      forsaken      forest,      \nour      once      vibrant      abode      now      stands      silent      and      still.",
        ]