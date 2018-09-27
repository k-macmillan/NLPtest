# pip install google-cloud-language
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types


def details(text):
    print(text)
    client = language.LanguageServiceClient()
    document = types.Document(content=text,
                              type=enums.Document.Type.PLAIN_TEXT)
    sentiment = client.analyze_sentiment(document=document).document_sentiment
    entities = client.analyze_entities(document).entities
    print('Sentiment:\n', sentiment)

    print('Entities:\n')
    # entity types from enums.Entity.Type
    entity_type = ('UNKNOWN', 'PERSON', 'LOCATION', 'ORGANIZATION',
                   'EVENT', 'WORK_OF_ART', 'CONSUMER_GOOD', 'OTHER')

    for entity in entities:
        print('=' * 20)
        print(u'{:<16}: {}'.format('name', entity.name))
        print(u'{:<16}: {}'.format('type', entity_type[entity.type]))
        print(u'{:<16}: {}'.format('metadata', entity.metadata))
        print(u'{:<16}: {}'.format('salience', entity.salience))
        print(u'{:<16}: {}'.format('wikipedia_url',
                                   entity.metadata.get('wikipedia_url', '-')))

    #   document.type == enums.Document.Type.HTML
    print('Tags of content:\n')
    tokens = client.analyze_syntax(document).tokens

    # part-of-speech tags from enums.PartOfSpeech.Tag
    pos_tag = ('UNKNOWN', 'ADJ', 'ADP', 'ADV', 'CONJ', 'DET', 'NOUN', 'NUM',
               'PRON', 'PRT', 'PUNCT', 'VERB', 'X', 'AFFIX')

    parse_tokens = []
    for token in tokens:
        print(u'{}: {}'.format(pos_tag[token.part_of_speech.tag],
                               token.text.content))
        parse_tokens.append(token.text.content)

    # The sections below failed, I didn't go into why they failed because I
    # don't think they are necessary for our project.

    # Detect and send native Python encoding to receive correct word offsets.
    # encoding = enums.EncodingType.UTF32
    # if sys.maxunicode == 65535:
    #     encoding = enums.EncodingType.UTF16

    # result = client.analyze_entity_sentiment(document, encoding)

    # for entity in result.entities:
    #     print('Mentions: ')
    #     print(u'Name: "{}"'.format(entity.name))
    #     for mention in entity.mentions:
    #         print(u'  Begin Offset : {}'.format(mention.text.begin_offset))
    #         print(u'  Content : {}'.format(mention.text.content))
    #         print(u'  Magnitude : {}'.format(mention.sentiment.magnitude))
    #         print(u'  Sentiment : {}'.format(mention.sentiment.score))
    #         print(u'  Type : {}'.format(mention.type))
    #     print(u'Salience: {}'.format(entity.salience))
    #     print(u'Sentiment: {}\n'.format(entity.sentiment))

    # categories = client.classify_text(document).categories

    # for category in categories:
    #     print(u'=' * 20)
    #     print(u'{:<16}: {}'.format('name', category.name))
    #     print(u'{:<16}: {}'.format('confidence', category.confidence))


if __name__ == '__main__':
    # details('What\'s going on in the nba with the lakers?')
    # details('What\'s going on today, excluding Trump?')
    # details('What new technology is there?')
    # details('How about them Lakers? Remove posts small posts and those ' +
            # 'with Lebron James')
    details('Add posts from subreddit nba or subreddit basketball matching ' +
            'Lakers without Lebron')
