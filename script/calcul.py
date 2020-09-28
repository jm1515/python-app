import matplotlib.pyplot as plt
import pandas as panda


class Calcul:
    """
    Cette classe permet de manipuler les données du Filereader.

    L'objectif de cette classe est de pouvoir effectuer les
    calculs en manipulant les données du dataframe.
    """

    def __init__(self, filereader):
        """ Constructeur de la classe Filereader

        On récupère le dataframe via notre objet Filereader passé en paramètre
        On initialise les attributs à vide """

        self.df = filereader.get_data()
        self.var_columns_qualitative = self.df.select_dtypes(include=['object']).columns.tolist()
        self.var_columns_quantitative = self.df.select_dtypes(include=['float64', 'int64']).columns.tolist()
        self.plot_quantitative = ""

    def get_nb_var(self):
        """ Cette fonction permet de retourner le nombre de variable. """

        return len(self.df.columns)

    def get_nb_observation(self):
        """ Cette fonction permet de retourner le nombre d'observation """

        return self.df.index.size

    def get_nb_var_qualitative(self):
        """ Cette fonction permet de retourner le nombre de variables qualitatives

        On récupère les variables dont les données correspondent à des chaînes de caractères
        Le type correspondant à une chaîne de caractère pour un dataframe est le type object """

        return len(self.var_columns_qualitative)

    def get_var_qualitative(self):
        """ Cette fonction permet de retourner les variables qualitatives """

        return str(self.var_columns_qualitative).replace('[', '').replace(']', '')

    def get_nb_var_quantitative(self):
        """ Cette fonction permet de retourner le nombre de variables quantitatives

        On récupère les variables dont les données correspondent à des valeurs numériques
        On précise qu'il peut s'agir soit d'un int, soit d'un float """

        return len(self.var_columns_quantitative)

    def get_var_quantitative(self):
        """ Cette fonction permet de retourner les variables quantitatives """

        return str(self.var_columns_quantitative).replace('[', '').replace(']', '')

    def get_info_var_qualitative(self):
        """ Cette fonction permet de retourner les informations associées aux variables qualitatives

        Grâce aux différentes fonctions et attributs associées au dataframe, on récupère les informations relatives
        aux variables qualitatives, et on les met en forme
        value_counts : retourne le nombre de fois où une donnée est présente dans le fichier """

        info = ""
        for var in self.var_columns_qualitative:
            info += "Variable : {} \nValeurs : {} \nFréquences : {} \n".format(var, str(self.df.get(var).value_counts().index.values).replace(' ', ', '),
                                                                        str(self.df[var].value_counts(normalize=True).values).replace(' ', ', '))
            info += "Nombre de modalités : " + str(len(self.df.get(var).value_counts().index.values)) + "\n"
            info += "Effectif : " + str(len(self.df.get(var))) + "\n \n"
        return info.replace('[', '').replace(']', '')

    def plot_var_qualitative(self):
        """ Cette fonction permet de générer un graphe à partir des informations relatives aux
            variables qualitatives

        On récupère toutes les données des variables qualitatives sous forme d'une liste,
        on les rassemble en les concaténant depuis la liste,
        et on génère le graphe, qui comprendra les fréquences associées à chaque valeur """

        i = 0
        df = self.df
        df_list = list()
        for var in self.var_columns_qualitative:
            partitionned_df = df.get(var).value_counts(normalize=True).to_frame()
            df_list.insert(i, partitionned_df)
            i += 1
        j = 0
        data_qualitative_final = ""
        for value in df_list:
            if j == 0:
                data_qualitative_final = value
            else:
                data_qualitative_final = panda.concat([data_qualitative_final, value], sort=False)
            j += 1
        data_qualitative_final.plot(kind='bar', figsize=(13, 7))
        plt.xticks(rotation=0)
        plt.legend(loc='upper left')
        plt.xlabel('Valeurs')
        plt.ylabel('Fréquences')
        plt.savefig('plot_data_qualitative.png')
        plt.close()

    def get_info_var_quantitative(self):
        """ Cette fonction permet de retourner les informations associées aux variables qualitatives

        Les différentes fonctions du dataframe nous permettent de récupérer les valeurs minimales (df.min()),
        maximales (df.max()), la médiane (df.median()), la moyenne (df.mean()), et l'écart-type (df.std()) """

        info = ""
        for var in self.var_columns_quantitative:
            info += "Variable : " + var + "\n"
            info += "Valeur minimale : " + str(self.df[var].min()) + "\n"
            info += "Valeur maximale : " + str(self.df[var].max()) + "\n"
            info += "Médiane : " + str(self.df[var].median()) + "\n"
            info += "Moyenne : " + str(self.df[var].mean()) + "\n"
            info += "Ecart-type : " + str(self.df[var].std()) + "\n \n"
        return info

    def plot_var_quantitative(self):
        """ Cette fonction permet de générer un graphe à partir des informations relatives aux
            variables quantitatives """

        plt.figure(figsize=(13, 7))
        self.df.mean().plot(kind='bar', label='moyenne', color='C9')
        self.df.std().plot(kind='line', label='écart-type', color='red')
        self.df.median().plot(kind='line', label='médiane', color='yellow')
        self.df[self.var_columns_quantitative].min().plot(kind='line', label='min', color='green')
        self.df[self.var_columns_quantitative].max().plot(kind='line', label='max', color='orange')
        plt.legend(loc='upper right')
        plt.xlabel('Variables')
        plt.savefig('plot_data_quantitative.png')
        plt.close()
