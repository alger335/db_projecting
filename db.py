db = 'postgresql://postgres:admin@localhost:5432/postgres'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()
artists_list = ['Meshuggah', 'TesseracT', 'Scar Symmetry',
                'Arch Enemy', 'Fear Factory', 'Disturbed',
                'Slipknot', 'Children of Bodom']

genres_list = ['Math metal', 'Melodic death', 'Industrial metal',
                'Metalcore', 'Nu metal']

albums_list = ['Obzen', 'One', 'Pitch Black Progress',
                'Anthems of Rebellion', 'Genexus', 'Immortalized', 'Slipknot', 'Follow The Reaper']

tracks_list = ['Combustion', 'Electric Red', 'Bleed', 'Lethargica', 'Obzen',
               'This Spiteful Snake', 'Pineal Gland Optics', 'Pravus', 'Dancers to a Discordant System',
               'Lament', 'Nascent', 'Acceptance - Concealing Fate, Pt.1', 'Deception - Concealing Fate, Pt.2',
               'The Impossible - Concealing Fate, Pt.3', 'Perfection - Concealing Fate, Pt.4',
               'Epiphany - Concealing Fate, Pt.5', 'Origin - Concealing Fate, Pt.6', 'Sunrise', 'April',
               'Eden', 'The Illusionist', 'Slaves to the Sublimal', 'Mind Machine', 'Pitch Black Progress',
               'Calculate the Apocalypse', 'Dreaming 24/7', 'Abstracted', 'The Kaleidoscopic God',
               'Retaliator', 'Oscillation Point', 'The Path of Least Resistance', 'Carved in Stone',
               'Deviate from the Form']

for a in artists_list:
    connection.execute(f"INSERT INTO Artist VALUES({a});")
