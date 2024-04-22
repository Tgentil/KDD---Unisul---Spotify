import pandas as pd

    # Remover coluna 'Unnamed: 0'
def clean_data(file_path):
    data = pd.read_csv(file_path)
    data.drop(columns=['Unnamed: 0'], inplace=True)

    # Função para limpar e converter colunas numéricas
    def clean_numeric(column):
        cleaned = pd.to_numeric(data[column].astype(str).str.extract(
            r'([-+]?\d*\.\d+|\d+)')[0], errors='coerce')
        return cleaned

    # Converter duração de ms para minutos e segundos
    def convert_duration(duration_ms):
        minutes = duration_ms // 60000
        seconds = (duration_ms % 60000) // 1000
        return f"{int(minutes)}m {int(seconds)}s"

    # Mapear valores de 'key' para notas musicais
    key_map = {-1: 'No Key', 0: 'C', 1: 'C♯/D♭', 2: 'D', 3: 'D♯/E♭', 4: 'E',
                5: 'F', 6: 'F♯/G♭', 7: 'G', 8: 'G♯/A♭', 9: 'A', 10: 'A♯/B♭', 11: 'B'}

    # Converter e categorizar atributos com base em seus intervalos
    def categorize_attribute(value, thresholds, categories):
        if pd.isnull(value):
            return "No Information"
        for threshold, category in zip(thresholds, categories):
            if value < threshold:
                return category
        return categories[-1]

    # Aplicar limpeza numérica
    numeric_columns = ['song_popularity', 'song_duration_ms', 'acousticness', 'danceability',
                        'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'audio_valence']
    for col in numeric_columns:
        data[col] = clean_numeric(col)

    # Converter 'song_duration_ms' para formato legível
    data['song_duration_ms'] = data['song_duration_ms'].apply(convert_duration)

    # Mapear 'key' para notas musicais
    data['key'] = data['key'].map(key_map)

    # Tratamento especial para 'audio_mode'
    mode_map = {'0': 'Minor', '1': 'Major',
                '0.105': 'Invalid Number', 'nao_sei': 'No Information'}
    data['audio_mode'] = data['audio_mode'].replace(mode_map)

    # Categorizar 'song_popularity 'acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'speechiness', 'audio_valence'
    attribute_thresholds = {
        'song_popularity': [25, 50, 75],
        'acousticness': [0.25, 0.50, 0.75],
        'danceability': [0.25, 0.50, 0.75],
        'energy': [0.25, 0.50, 0.75],
        'instrumentalness': [0.1, 0.5, 0.9],
        'liveness': [0.2, 0.6, 0.8],
        'loudness': [-60, -30, -15, -5, 0],
        'speechiness': [0.33, 0.66, 1.0],
        'tempo': [60, 120, 160],
        'audio_valence': [0.25, 0.50, 0.75]
    }
    attribute_categories = {
        'song_popularity': ["Low", "Moderate", "High", "Very High"],
        'acousticness': ["Poor", "Below Average", "Above Average", "Excellent"],
        'danceability': ["Low", "Moderate", "High", "Very High"],
        'energy': ["Low", "Moderate", "High", "Very High"],
        'instrumentalness': ["None", "Some", "Significant", "Strong"],
        'liveness': ["Studio", "Some Audience", "High Live", "Live"],
        'loudness': ["Very Quiet", "Quiet", "Moderate", "Loud", "Very Loud"],
        'speechiness': ["Music", "Mixed", "Speech", "Talk"],
        'tempo': ["Slow", "Moderate", "Fast"],
        'audio_valence': ["Sad", "Neutral", "Happy", "Very Happy"]
    }
    for attribute, thresholds in attribute_thresholds.items():
        data[attribute] = data[attribute].apply(
            categorize_attribute, args=(thresholds, attribute_categories[attribute]))

        # Tratamento especial para 'time_signature'
    def clean_time_signature(signature):
        if pd.isnull(signature) or signature == 'nao_sei':
            return "No Information"
        signature = float(signature)
        if signature.is_integer() and 3 <= signature <= 7:
            return int(signature)
        else:
            return "Invalid Number"

    data['time_signature'] = data['time_signature'].apply(clean_time_signature)

    return data


# Caminhos dos arquivos
input_file_path = 'data/spotify1_20240415200237.csv'
output_file_path = 'out/cleaned_spotify_data.xlsx'

# Limpar os dados
cleaned_data = clean_data(input_file_path)

# Salvar os dados limpos em um arquivo XLSX
cleaned_data.to_excel(output_file_path, index=False)

print("Dados limpos salvos com sucesso em:", output_file_path)
