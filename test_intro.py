import os
import sys


CACHE_CATALOG = os.getcwd() + "/.model_cache"

if __name__ == '__main__':
    if sys.prefix == sys.base_prefix:
        print('\U0001F44E Ten plik należy uruchomić w wirtualnym środowisku Pythona. Punkt 1 instrukcji w pliku README.md')
        sys.exit(1)
    else:
        print('\U0001F44D Skrypt uruchomiony w wirtualnym środowisku Pythona')

    try:
        import openai
        print('\U0001F44D openai zainstalowane')
    except ImportError:
        print('\U0001F44E openai nie zainstalowane. Zainstaluj pakiety z pliku requirements.txt. Punkt 5 instrukcji w pliku README.md')
        sys.exit(1)

    try:
        from langchain.llms import OpenAI
        print('\U0001F44D langchain zainstalowane')
    except ImportError:
        print('\U0001F44E langchain nie zainstalowane. Zainstaluj pakiety z pliku requirements.txt. Punkt 5 instrukcji w pliku README.md')
        sys.exit(1)

    try:
        import transformers
        print('\U0001F44D transformers zainstalowane')
    except ImportError:
        print('\U0001F44E transformers nie zainstalowane. Zainstaluj pakiety z pliku requirements.txt. Punkt 5 instrukcji w pliku README.md')
        sys.exit(1)

    try:
        import torch
        print('\U0001F44D PyTorch zainstalowane')
    except ImportError:
        print('\U0001F44E PyTorch nie zainstalowane. Zainstaluj pakiety z pliku requirements.txt. Punkt 5 instrukcji w pliku README.md')
        sys.exit(1)

    try:
        import wikipedia
        print('\U0001F44D wikipedia zainstalowane')
    except ImportError:
        print('\U0001F44E wikipedia nie zainstalowane. Zainstaluj pakiety z pliku requirements.txt. Punkt 5 instrukcji w pliku README.md')
        sys.exit(1)

    if os.path.exists(CACHE_CATALOG):
        print('\U0001F44D Katalog cache już istnieje')
    else:
        print('Tworzenie katalogu cache z modelem GPT-2, którego użyjemy jako przykładu open-sourcowego modelu...')
        os.mkdir(CACHE_CATALOG)

    print('Ścieżka do katalogu cache: ' + CACHE_CATALOG)
    print('Jeżeli pojawia się błąd, upewnij się, że ścieżka do katalogu cache jest poprawna i nie zawiera spacji')

    os.environ['TRANSFORMERS_CACHE'] = CACHE_CATALOG
    try:
        from langchain import HuggingFacePipeline
        llm = HuggingFacePipeline.from_model_id(
            model_id="gpt2",
            task="text-generation",
            model_kwargs={"temperature":0.1, "cache_dir":CACHE_CATALOG},
            pipeline_kwargs={"do_sample":True, "max_new_tokens":50}
        )
        llm("To jest przykładowy tekst, który")  # wynik nie ma znaczenia, chcemy wiedzieć czy zadziałało
        print('\U0001F44D Katalog cache utworzony')
    except Exception as e:
        print('\U0001F44E Nie udało się utworzyć katalogu cache.')
        print('Sprawdź czy jest wystarczająco dużo miejsca na dysku i czy ścieżka do katalogu cache jest poprawna i nie zawiera spacji')
        print('Jeśli wszystko wygląda prawidłowo, ale nadal nie działa, rozwiążemy ten problem w czasie zajęć.')
        print('Błąd:')
        print(e)
        sys.exit(1)

    print("\U0001F44D \U0001F44D \U0001F44D DZIAŁA!")
    sys.exit(0)
