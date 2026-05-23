# Madlibs is a game where you are asked to choose from a variety of different words to create a story.
# Madlibs is a common practice project idea in the coding world.

story = int(input("Enter a number between 1-2"))

if story == 1:
    # Collecting lots more words
    adj1 = input("Enter an adjective: ")
    adj2 = input("Enter another adjective: ")
    adj3 = input("Enter another adjective: ")
    adj4 = input("Enter another adjective: ")
    adj5 = input("Enter another adjective: ")

    verb1 = input("Enter a verb: ")
    verb2 = input("Enter another verb: ")
    verb3 = input("Enter another verb: ")
    verb4 = input("Enter another verb: ")

    noun1 = input("Enter a noun: ")
    noun2 = input("Enter another noun: ")
    noun3 = input("Enter another noun: ")
    noun4 = input("Enter another noun: ")

    place1 = input("Enter a place: ")
    emotion1 = input("Enter an emotion: ")

    print(f"""
    Once upon a time, in the incredibly {adj1}, strangely {adj2}, and slightly {adj3} halls of {place1},
    there lived a determined student named {noun1}. Every morning, {noun1} would {verb1} through the crowded
    hallways, clutching a {adj4} notebook and a mysteriously {adj5} pencil.

    On one particularly stressful day, {noun1} entered the classroom to take a very important Algebra 2 test,
    a test rumored to challenge even the most {adj1} and {adj2} minds. The test focused on how complicated
    equations and variables connected in ways that felt both magical and frustrating.

    As the clock ticked loudly and dramatically, {noun1} began to feel {emotion1}. Instead of calmly solving
    the equations, {noun1} made a questionable decision—to {verb2} on the test. Slowly, carefully, and a bit
    dramatically, {noun1} glanced over at {noun2}, who was confidently writing answers with a {adj3} grin.

    Trying not to get caught, {noun1} attempted to {verb3} answers while pretending to {verb4} intensely at
    their own paper. Unfortunately, the teacher, a very observant and slightly {adj4} figure, noticed the
    suspicious behavior immediately.

    The consequences were swift, serious, and undeniably {adj5}. {noun1} received an F and was asked to stay
    after class. Sitting alone with only a {noun3} and a very quiet {noun4} nearby, {noun1} began to reflect
    deeply on the choices that had been made.

    “Why did I choose to {verb2} instead of studying?” {noun1} wondered aloud, dramatically staring into the
    distance as if in a movie scene. The lesson was clear, powerful, and a little bit {adj2}: hard work,
    honesty, and effort matter far more than shortcuts.

    From that day forward, {noun1} promised to never repeat the same mistake. Instead, they would {verb1},
    {verb3}, and even {verb4} their way through future challenges—with determination, integrity, and maybe
    just a little bit of humor.

    And so, in the same {adj1} and {adj3} school where it all began, {noun1} slowly transformed into a wiser,
    more responsible student—one who always remembered to put the fries in the bag... but only after earning them.
    """)