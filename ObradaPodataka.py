import pickle
import numpy as np

# Ucitavanje podataka
with open('dataset.pickle', 'rb') as f:
    data = pickle.load(f)

# Funkcija koja vraca duljinu timestempova
def get_ts_duration(key, content_type):
    durations = []

    # Dohvacanje duljine trajanja unosa svake rijeci, fraze i slova svakog korisnika
    for input_mode in ["Finger", "Stylus"]:
            for content_id in content_type:
                if key in data and input_mode in data[key] and "tablet" in data[key][input_mode]:
                    if str(content_id) in data[key][input_mode]["tablet"]:
                        input_data = data[key][input_mode]["tablet"][str(content_id)]

                        timestamps = input_data['data']['ts']
                        durations.append(len(timestamps))
    return durations

# Funkcija za normalizaciju podataka
def normalize_data(users, content_type, median_duration):
    for user in users:
        for input_mode in ["Finger", "Stylus"]:
            for content_id in content_type:
                if user in data and input_mode in data[user] and "tablet" in data[user][input_mode]:
                    if str(content_id) in data[user][input_mode]["tablet"]:
                        input_data = data[user][input_mode]["tablet"][str(content_id)]
    
                        timestamps = input_data['data']['ts']
                        if((np.array(timestamps)).any()):
                            normalized_timestamps = np.linspace(int(timestamps[0]), int(timestamps[-1]), median_duration)
                            #print(timestamps)
                            data[user][input_mode]['tablet'][str(content_id)]['data']['ts'] = normalized_timestamps
                            #print(np.ndim(input_data['data']['magX']))

                        for key in ['rawposX', 'rawposY', 'relposX', 'relposY', 'velX', 'velY', 'magX', 'magY', 'magZ', 'orientation', 'pressure', 'size']:
                            values = input_data['data'][key]
                            if((np.array(values)).any()):
                                interpolated_values = np.interp(normalized_timestamps, timestamps, values)
                                data[user][input_mode]['tablet'][str(content_id)]['data'][key] = interpolated_values

median_duration_letter_array=[]
median_duration_word_array=[]
median_duration_phrase_array=[]
for user in range(20):
    durations_letter = get_ts_duration(user, range(126, 312))
    median_duration_letter = int(np.median(durations_letter))
    median_duration_letter_array.append(median_duration_letter)

    durations_word = get_ts_duration(user, range(76, 126))
    median_duration_word = int(np.median(durations_word))
    median_duration_word_array.append(median_duration_word)
    
    durations_phrase = get_ts_duration(user, range(26, 77))
    median_duration_phrase = int(np.median(durations_phrase))
    median_duration_phrase_array.append(median_duration_phrase)
    #print("slova",median_duration_letter)

median_letter = int(np.median(median_duration_letter_array))
print(median_letter)
median_word = int(np.median(median_duration_word_array))
print(median_word)
median_phrase = int(np.median(median_duration_phrase_array))
print(median_phrase)

normalize_data(range(20), range(126, 312), median_letter)
normalize_data(range(20), range(76, 126), median_word)
normalize_data(range(20), range(26, 77), median_phrase)

#with open('example.txt', 'w') as file:
    #file.write(str(data))

#with open('data.pkl', 'wb') as file:
   # pickle.dump(data, file)
  #  file.close()