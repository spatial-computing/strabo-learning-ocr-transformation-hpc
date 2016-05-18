import pickle


if __name__ == '__main__':
    f = pickle.load(open('gbc_model.pkl', 'rb'))
    print('Done.')