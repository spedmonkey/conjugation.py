import pandas as pd
import random as random

'''
https://www.sketchengine.eu/spanish-word-list/#tab-id-4-active verbs with number of frequencies
C:\conjugation\Scripts\python.exe C:/Users/gime9/PycharmProjects/conjugation/conjugation.py
Index(['infinitive', 'infinitive_english', 'mood', 'mood_english', 'tense',
       'tense_english', 'verb_english', 'form_1s', 'form_2s', 'form_3s',
       'form_1p', 'form_2p', 'form_3p', 'gerund', 'gerund_english',
       'pastparticiple', 'pastparticiple_english', 'importance'],
      dtype='object')
'''
class Conjugation(object):
	def __init__(self):
		verbs_df = self.load_dfs()
		frequency_list = []


		#verbs_df.to_pickle('/Users/gime9/PycharmProjects/conjugation/verbs_pickle.pkl')
		#verbs_df= verbs_df[verbs_df['tense'] == "Presente"]
		self.start_event_loop(verbs_df)

	def start_event_loop(self, verbs_df):
		replace_character_list = [('á','a'),('é','e'),('í','i'),('ó','o'),('ú','u'),('ü','u'),('ñ','n')]
		verb_list = []
		verb_frequency_picker = []

		for index, row in enumerate(verbs_df['form_1s']):
			if (verbs_df['tense_english'][index]) != "Present":
				continue
			if (verbs_df['mood'][index]) == "Subjuntivo":
				continue
			verb_list.append(row)
			verb_frequency_picker.append(verbs_df['frequency'][index])

		random_verb = (random.choices(verb_list, weights = verb_frequency_picker))[0]
		english_random_verb = random_verb

		infinitive = verbs_df[(verbs_df.values.ravel() == random_verb).reshape(verbs_df.shape).any(1)]['infinitive'].values
		if infinitive.size  == 0:
			self.start_event_loop(verbs_df)


		# print ( verbs_df[(verbs_df.values.ravel() == random_verb).reshape(verbs_df.shape).any(1)].values )
		print(verbs_df[(verbs_df.values.ravel() == random_verb).reshape(verbs_df.shape).any(1)]['infinitive'].values,
			  verbs_df[(verbs_df.values.ravel() == random_verb).reshape(verbs_df.shape).any(1)]['tense_english'].values,
			  verbs_df[(verbs_df.values.ravel() == random_verb).reshape(verbs_df.shape).any(1)]['infinitive_english'].values,
			  verbs_df[(verbs_df.values.ravel() == random_verb).reshape(verbs_df.shape).any(1)]['verb_english'].values)
		# print (verbs_df[(verbs_df.values.ravel() == random_verb).reshape(verbs_df.shape).any(1)].columns )


		var = input("Please enter something: ")
		print("You entered: " + var)

		for character in replace_character_list:
			english_var = self.replace_characters(var, character[0], character[1])
			english_random_verb =  self.replace_characters(english_random_verb, character[0], character[1])
		print ("replaced string", english_var, english_random_verb)

		if  (english_var == english_random_verb):
			print (f"{bcolors.OKGREEN}Correct:{bcolors.ENDC} you entered: {english_var} verb is: {random_verb}")
		else:
			print (f"{bcolors.WARNING}Incorrect:{bcolors.ENDC} you entered: {0} verb is: {1}".format(english_var, random_verb))
		print ("=============================================================================================")
		self.start_event_loop(verbs_df)

	def load_dfs(self):
		#verbs_df = pd.read_csv("C:/Users/gime9/PycharmProjects/conjugation/jehle_verb_database.csv")
		#verbs_pickle.pkl

		verbs_df = pd.read_pickle(('/Users/gime9/PycharmProjects/conjugation/verbs_pickle.pkl'))
		#verbs_in_order = pd.read_csv("C:/Users/gime9/PycharmProjects/conjugation/verbs_with_frequencies.csv")
		return verbs_df

	@staticmethod
	def replace_characters(verb, spanish_character, english_character):
		verb = verb.replace(spanish_character, english_character)
		return verb

	@staticmethod
	def print_df(df):
		for index, row in df.iterrows():
			print (index, row)

	@staticmethod
	def return_frequency(verbs_in_order, row):
		return (verbs_in_order.iloc[row, 1])

	@staticmethod
	def return_unique_verbes(verbs_df):
		return ( verbs_df['infinitive'].unique() )

	@staticmethod
	def return_rows(verbs_df, infinitive_verb):
		return ((verbs_df.loc[verbs_df['infinitive'] == infinitive_verb]).index.to_numpy())

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


Conjugation = Conjugation()

'''
for index, row in verbs_df.iterrows():
	infinitive = (row['infinitive'])
	if self.return_rows(verbs_in_order, infinitive).size > 0:
		row_frequency = self.return_rows(verbs_in_order, infinitive)
		frequency = self.return_frequency(verbs_in_order, row_frequency).values[0]
		frequency = int(frequency.replace(' ',''))
	else:
		frequency = 5000
	frequency_list.append(frequency)

verbs_df.insert(17, "frequency", frequency_list, True)
'''