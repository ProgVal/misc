#!/usr/bin/env python3

verbes_sans_sujet = set((
#        Singulier                  Pluriel                     Accepte COD
        ('cliquez',                 'cliquez',                  True),
        ('gagnez',                  'gagnez',                   True),
        ('prévoir',                 'prévoir',                  True),
        ('acheter',                 'acheter',                  True),
        ('voyagez',                 'voyagez',                  False),
    ))
CODs = set((
        'le paypal',
        'l’offre payante',
        'le 1.000.000ème visiteur',
        'la connexion',
        'sur partenariat',
        'déblocage du adblock',
        'la concurrence',
    ))

sujets = set((
#        Singulier                  Pluriel
        ('le cheminement de fer',   'les cheminement de fer'),
        ('le RFC',                  'les RFC',),
        ('Blogzmeyer',              None),
    ))
verbes_avec_sujet = set((
#        Singulier                  Pluriel                     Accepte COD
        ('est',                     'sont',                     False),
        ('balaye',                  'balayent',                 True),
    ))
modaux = set((
#        Modal                      Accepte "petits caractères"
        ('en illimité',             True),
        ('pas cher',                False),
        ('dans la limite de stock', False),
    ))
petits_caractères = set((
        '(¹)',
        '(*)',
        ' (sous condition)',
    ))

compléments_temps = set((
        'toute la saison',
        'jusqu’à 4 years ago',
        'pendant 10.0.00000.000 minutes sur batterie',
        'à la vitesse supérieure',
        None,
    ))
buts = set((
        'pour abonnement gratuit',
        'pour abonnement premier',
        'pour administrement',
        'pour inscrivage en connexion',
        'pour obtenir sextape',
        'pour réseau élite',
        'pour retruiter une personne',
        'pour transfert d’héritage',
    ))
suites_but = set((
        'de les internet',
        'des billets de wagon',
        'de la Russie',
        'de célibataires avec exigence',
        'à -10.0000000000000.00000000%%% de réduction',
    ))
avec = set((
        'grâce à web',
        'grâce à hacker chinois corrompu',
        'avec livraison sur VPN',
        'en collaborant avec socialisme de nation',
        'avec docteur du mollusque',
        'avec partenariat AMD/ATI',
        'dans votre région France (Toulouse)',
        'et 10000000.0.0.000000000000000.0.0..0.0....0000....000%€ des gagnants (+ les perdants!!!) ont gagné',
    ))

import random

def construire(one=False):
    phrases = set()
    if one:
        if random.randint(0, 1):
            return construire_sans_sujet(one)
        else:
            return construire_avec_sujet(one)
    return construire_sans_sujet(one) | construire_avec_sujet(one)

def construire_sans_sujet(one):
    phrases = set()
    for (verbe_sing, verbe_plur) in construire_verbe_et_modal(verbes_sans_sujet, one):
        for suite in construire_suite_verbe(one):
            if one:
                if random.randint(0, 1):
                    return set([verbe_sing + ' ' + suite])
                else:
                    return set([verbe_plur + ' ' + suite])
            else:
                phrases.add(verbe_sing + ' ' + suite)
                phrases.add(verbe_plur + ' ' + suite)
    return phrases

def construire_avec_sujet(one):
    phrases = set()
    for (sujet_sing, sujet_plur) in sujets:
        for (verbe_sing, verbe_plur) in construire_verbe_et_modal(verbes_avec_sujet, one):
            for suite in construire_suite_verbe(one):
                if sujet_plur:
                    debut = sujet_plur + ' ' + verbe_plur
                else:
                    debut = sujet_sing + ' ' + verbe_sing
                if one:
                    return set([debut + ' ' + suite])
                else:
                    phrases.add(debut + ' ' + suite)
    return phrases

def construire_modaux(one):
    phrases = set()
    for (modal, accepte_petits_caractères) in modaux:
        phrases.add(modal)
        if accepte_petits_caractères:
            for petits_caractères_ in petits_caractères:
                if one:
                    return set([modal + petits_caractères_])
                else:
                    phrases.add(modal + petits_caractères_)
    return phrases

def construire_verbe_et_modal(verbes, one):
    phrases = set()
    for (verbe_sing, verbe_plur, transitif) in verbes:
        phrases.add((verbe_sing, verbe_plur))
        for modal in construire_modaux(one):
            modal = ' ' + modal if modal else ''
            phrases.add((verbe_sing + modal, verbe_plur + modal))
        if transitif:
            for COD in CODs:
                phrases.add((verbe_sing + ' ' + COD, verbe_plur + ' ' + COD))
                for modal in construire_modaux(one):
                    modal = ' ' + modal if modal else ''
                    phrases.add((verbe_sing + modal + ' ' + COD, verbe_plur + modal + ' ' + COD))
        if one:
            return phrases
    return phrases

def construire_suite_verbe(one):
    phrases = set()
    for compl_temps in compléments_temps:
        for but in buts:
            for suite_but in suites_but:
                for avec_ in avec:
                    phrases.add((compl_temps + ' ' if compl_temps else '') +
                                but + ' ' + suite_but +
                                (' ' + avec_ if avec_ else ''))
                    if one:
                        return phrases
    return phrases

if __name__ == '__main__':
    import sys
    format_ = lambda x:x.upper()+' '+('!'*random.randint(1, 9))
    if '--one' in sys.argv:
        print(list(map(format_, construire(one=True)))[0])
    else:
        try:
            print('\n'.join(map(format_, construire())))
        except KeyboardInterrupt:
            print('')
            exit()

