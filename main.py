import General
import Pickler

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    g_laender_factory = General.GAlleLaenderFactory()
    Pickler.pickle_all(g_laender_factory)
