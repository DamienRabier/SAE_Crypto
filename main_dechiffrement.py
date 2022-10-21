# importer le fichier dechiffrement_affine.py du dossier Dechiffrement
from Dechiffrement.dechiffrement_affine import *
from Dechiffrement.dechiffrement_cesar import *
from Dechiffrement.dechiffrement_vigenere import *

texte_1 ="Huyzu Izxk u'hoovihvy eht h wzopvo. Vk hkkdph. Tzu Ahc phojdhvy pvudvy ivuly. Vk ezdtth du eozgzuw tzdevo, t'httvy whut tzu kvy, t'heedxhuy tdo tzu ezkzrqzu. Vk eovy du ozphu, vk k'zdiovy, vk kdy; phvt vk u'x thvtvtthvy jd'du vpmozlkvz rzugdt, vk mdyhvy h yzdy vutyhuy tdo du pzy wzuy vk vluzohvy kh tvluvgvrhyvzu. Vk hmhuwzuuh tzu ozphu tdo tzu kvy. Vk hkkh h tzu khihmz; vk pzdvkkh du lhuy jd'vk ehtth tdo tzu gozuy, tdo tzu rzd."
texte_2 ="Dwi gsftn seebvzx ezjg jzzo. Zp ldvzx npvlh. Tt jlzcqo jsy dvjmdbvj, wnzpke wi ilme. Qg wetavzx owpo. Yy jmlme qiumdbdege ujexlqo uy qipssfzb. Lr nimzpwwi, gpfa gfycl ll'yy ogrw, atpj wzcmu uf'ci ksnade, twcn gvznjeh bc'pe fzcmusy, vje pzqi, jsyvv kvzqn tsfxn. Uy niirp Didex-Ximkmy, ci tplxjkmd xgrmybdw wtoirplqo lr npvceyl llm ainjetb."
texte_3 ="Sop u'dffrmtfe oz qvigpjcm, bh nnaqhd iw hcbvrl dvercy, h d'youcxlmdc zpzirn, ay eg xpzzht, qy eg xohirgxpb, ymsu lstlhf bh zhkhakc, z'lbnnecvz, layoanfe bh bidv g'dlky. Oy x'txdwiyoh, gnvxnnt w'txwlkhr g'bh uuhr oju, nyor v'nnaqhd dwvz akl ojr, erdpzhyomennv innr vn nmim tqvfe om'xl yof qv x'cmksxluzf."
texte_4 = "Zc krgfkr u'le ufzxk le rzi drikzrc jli c'fscfex tyrjjzj ul mrjzjkrj.Zc flmizk jfe wizxf dlirc, zc gizk ul crzk wifzu, zc slk le xireu sfc. Zc j'rgrzjrzk. Zc j'rjjzk jli jfe tfjp, zc gizk le aflierc hl'zc gritflilk u'le rzi uzjkirzk. Zc rccldr le tzxrizccf hl'zc wldr aljhl'rl sflk hlfzhl'zc kiflmrk jfe griwld ziizkrek. Zc kfljjr."
texte_5 ="Os dom sb kbrog : wf bok bykg-ewzbof ywm lwoxo r'wf zglmgf, hwol wf mbfug, hwol wf ygv-mkgm, hwol wf egmossgf dol bw ugwm rw pgwk. Rwmkgfe eibfmb rw Sbfndbff, Zbkzbkb wf dbrkoubs r'Bkbugf, Lmoei-Kbfrbss wf bok r' Borb."

liste_T = [texte_1, texte_2, texte_4]


def liste_dechiffrement(texte):
    dechiffrement = [vigenere_inverse(texte,recherche_mot_cle(texte,longueur_cle(texte))),essaie_decriptage_cle("\n\n"+texte+"\n\n"),decoder_affine(texte,clé_affine(texte)[0],clé_affine(texte)[1])]
    return dechiffrement

    
    
    

def main():
    # Réalisation d'un menu d'options dans le terminal
    print("-------------------------------------------------------------")
    print("|                                                           |")
    print("|   Bienvenue dans le programme de déchiffrement de texte   |")
    print("|                                                           |")
    print("-------------------------------------------------------------")
    print("| 1 -           Déchiffrer tous les textes                  |")
    print("|                                                           |")
    print("| 2 -           Déchiffrer un texte                         |")
    print("|                                                           |")
    print("| 3 -          Dechiffrer un texte personnalisé             |")
    print("|                                                           |")
    print("| 4 -           Quitter le programme                        |")
    print("|                                                           |")
    print("-------------------------------------------------------------")
    choix = input("Entrez votre choix : ")
    if choix == "1":
        dictionnaire_reponse ={texte_1 : None, texte_2 : None, texte_3 : None, texte_4 : None, texte_5 : None}
        t= 0
        # Tant que le texte ne comporte pas plus de trois mots dans le dictionnaire francais Utilitaires/francais.txt, on continue à déchiffrer
        for i in range(len(liste_T)):
            listD = liste_dechiffrement(liste_T[i])
            while(compter_nb_mots_francais(separer_mots(listD[t])),"Utilitaires/francais.txt") < (len(separer_mots(listD[t])) / 3):
                t+=1
            dictionnaire_reponse[liste_T[i]] = listD[t]
            t=0
        print(dictionnaire_reponse)
                
                
    
    

    


    

    

if __name__ == '__main__':
    main() 