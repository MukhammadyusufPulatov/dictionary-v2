import requests


def getDefinitions(word_id):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word_id}"
    r = requests.get(url)
    res = r.json()
    if 'title' in res:
        return False
    output = {}
    deflar = []

    try:
        senses = res[0]['meanings'][0]['definitions']
        parts = res[0]['meanings'][0]
        deflar.append('Part of Speech: ' + parts['partOfSpeech'])
        for nouns in senses:
            deflar.append('❓ Definition:  ' + nouns['definition'])
            deflar.append('📝 Example: ' + nouns['example'])
    except:
        pass
    try:
        senses_verb = res[0]['meanings'][1]['definitions']
        deflar.append('Part of speech: ' + res[0]['meanings'][1]['partOfSpeech'])
        for verbs in senses_verb:
            deflar.append('❓ Definition:  ' + verbs['definition'])
            deflar.append('📝 Example: ' + verbs['example'])
    except:
        pass
    try:
        senses_adj = res[0]['meanings'][2]['definitions']
        deflar.append('Part of speech: ' + res[0]['meanings'][2]['partOfSpeech'])
        for adjectives in senses_adj:
            deflar.append('❓ Definition:  ' + adjectives['definition'])
            deflar.append('📝 Example: ' + adjectives['example'])

    except:
        pass
    output['def'] = '\n'.join(deflar)
    try:
        res[0]['phonetics'][0].get('audio')
        output['audio'] = res[0]['phonetics'][0]['audio']
    except:
        pass

    return output


if __name__ == '__main__':
    from pprint import pprint as print

    print(getDefinitions('preserve'))
