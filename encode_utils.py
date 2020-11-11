import skipthoughts.skipthoughts as skipthoughts

def skipthought_encode(answers):
    """
    Obtains sentence embeddings for each sentence in the emails
    """
    num_answers = len(answers)
    enc_answers = [None]*len(answers)
    cum_sum_sentences = [0]
    sent_count = 0

    for answer in answers:
      sent_count += len(answer)
      cum_sum_sentences.append(sent_count)

    all_sentences = [sent for answer in answers for sent in answer]
    print('Loading pre-trained models...')
    model = skipthoughts.load_model()
    encoder = skipthoughts.Encoder(model)
    print('Encoding sentences...')
    enc_sentences = encoder.encode(all_sentences, verbose=False)

    for i in range(len(answers)):
      begin = cum_sum_sentences[i]
      end = cum_sum_sentences[i+1]
      enc_answers[i] = enc_sentences[begin:end]
    return enc_answers
