# Lien du github:
https://github.com/cassandre18/big-data

# 1. Installation
installer Virtual Box et HDP Sandbox


# 2. configuration l'environnment de travail
charger le fichier dans Sandbox
faire attention à bine changer les paramètres

## 2.1 execution la vm
double cliquer sur la vm ou appuyer sur demarer 
la fenettre Hortonworks SandBox va s'ouvrir, attendre que tous se mettre en route et que l'url de Virtual BOX et l'url de VMWare s'affiche

# 3. Accéder au cluster HDP Sandbox
aller sur le lien 1080
metre le login mot de passe 
cliquer sur Ambari avec le port 8080 et attendre que tous soit en vert

## 3.1 accès ssh
### par le navigateur
Vous pouvez accéder au cluster via le client web shell ou appelé shell-in-a-box en suivant l'adresse http://localhost:4200 dans votre navigateur.
### par le terminal de commande
C:\Users\cassa>ssh maria_dev@localhost -p 2222
The authenticity of host '[localhost]:2222 ([127.0.0.1]:2222)' can't be established.
ED25519 key fingerprint is SHA256:7C3ELG2dUbGt7trSrxBYYsXHZHRprMe+UC0eIlkxTb0.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[localhost]:2222' (ED25519) to the list of known hosts.
maria_dev@localhost's password:
[maria_dev@sandbox-hdp ~]$


# 3.HDFS
## 3.1 Prise en main 
### question 1 : différence entre hadoop fs et hdfs dfs
#### avec hadoop fs
 hadoop fs
Usage: hadoop fs [generic options]
        [-appendToFile <localsrc> ... <dst>]
        [-cat [-ignoreCrc] <src> ...]
        [-checksum <src> ...]
        [-chgrp [-R] GROUP PATH...]
        [-chmod [-R] <MODE[,MODE]... | OCTALMODE> PATH...]
        [-chown [-R] [OWNER][:[GROUP]] PATH...]
        [-copyFromLocal [-f] [-p] [-l] <localsrc> ... <dst>]
        [-copyToLocal [-p] [-ignoreCrc] [-crc] <src> ... <localdst>]
        [-count [-q] [-h] [-v] [-t [<storage type>]] [-u] <path> ...]
        [-cp [-f] [-p | -p[topax]] <src> ... <dst>]
        [-createSnapshot <snapshotDir> [<snapshotName>]]
        [-deleteSnapshot <snapshotDir> <snapshotName>]
        [-df [-h] [<path> ...]]
        [-du [-s] [-h] <path> ...]
        [-expunge]
        [-find <path> ... <expression> ...]
        [-get [-p] [-ignoreCrc] [-crc] <src> ... <localdst>]
        [-getfacl [-R] <path>]
        [-getfattr [-R] {-n name | -d} [-e en] <path>]
        [-getmerge [-nl] <src> <localdst>]
        [-help [cmd ...]]
        [-ls [-C] [-d] [-h] [-q] [-R] [-t] [-S] [-r] [-u] [<path> ...]]
        [-mkdir [-p] <path> ...]
        [-moveFromLocal <localsrc> ... <dst>]
        [-moveToLocal <src> <localdst>]
        [-mv <src> ... <dst>]
        [-put [-f] [-p] [-l] <localsrc> ... <dst>]
        [-renameSnapshot <snapshotDir> <oldName> <newName>]
        [-rm [-f] [-r|-R] [-skipTrash] [-safely] <src> ...]
        [-rmdir [--ignore-fail-on-non-empty] <dir> ...]
        [-setfacl [-R] [{-b|-k} {-m|-x <acl_spec>} <path>]|[--set <acl_spec> <path>]]
        [-setfattr {-n name [-v value] | -x name} <path>]
        [-setrep [-R] [-w] <rep> <path> ...]
        [-stat [format] <path> ...]
        [-tail [-f] <file>]
        [-test -[defsz] <path>]
        [-text [-ignoreCrc] <src> ...]
        [-touchz <path> ...]
        [-truncate [-w] <length> <path> ...]
        [-usage [cmd ...]]

Generic options supported are
-conf <configuration file>     specify an application configuration file
-D <property=value>            use value for given property
-fs <local|namenode:port>      specify a namenode
-jt <local|resourcemanager:port>    specify a ResourceManager
-files <comma separated list of files>    specify comma separated files to be copied to the map reduce cluster
-libjars <comma separated list of jars>    specify comma separated jar files to include in the classpath.
-archives <comma separated list of archives>    specify comma separated archives to be unarchived on the compute machines.

#### avec hdfs dfs
 hdfs dfs
Usage: hadoop fs [generic options]
        [-appendToFile <localsrc> ... <dst>]
        [-cat [-ignoreCrc] <src> ...]
        [-checksum <src> ...]
        [-chgrp [-R] GROUP PATH...]
        [-chmod [-R] <MODE[,MODE]... | OCTALMODE> PATH...]
        [-chown [-R] [OWNER][:[GROUP]] PATH...]
        [-copyFromLocal [-f] [-p] [-l] <localsrc> ... <dst>]
        [-copyToLocal [-p] [-ignoreCrc] [-crc] <src> ... <localdst>]
        [-count [-q] [-h] [-v] [-t [<storage type>]] [-u] <path> ...]
        [-cp [-f] [-p | -p[topax]] <src> ... <dst>]
        [-createSnapshot <snapshotDir> [<snapshotName>]]
        [-deleteSnapshot <snapshotDir> <snapshotName>]
        [-df [-h] [<path> ...]]
        [-du [-s] [-h] <path> ...]
        [-expunge]
        [-find <path> ... <expression> ...]
        [-get [-p] [-ignoreCrc] [-crc] <src> ... <localdst>]
        [-getfacl [-R] <path>]
        [-getfattr [-R] {-n name | -d} [-e en] <path>]
        [-getmerge [-nl] <src> <localdst>]
        [-help [cmd ...]]
        [-ls [-C] [-d] [-h] [-q] [-R] [-t] [-S] [-r] [-u] [<path> ...]]
        [-mkdir [-p] <path> ...]
        [-moveFromLocal <localsrc> ... <dst>]
        [-moveToLocal <src> <localdst>]
        [-mv <src> ... <dst>]
        [-put [-f] [-p] [-l] <localsrc> ... <dst>]
        [-renameSnapshot <snapshotDir> <oldName> <newName>]
        [-rm [-f] [-r|-R] [-skipTrash] [-safely] <src> ...]
        [-rmdir [--ignore-fail-on-non-empty] <dir> ...]
        [-setfacl [-R] [{-b|-k} {-m|-x <acl_spec>} <path>]|[--set <acl_spec> <path>]]
        [-setfattr {-n name [-v value] | -x name} <path>]
        [-setrep [-R] [-w] <rep> <path> ...]
        [-stat [format] <path> ...]
        [-tail [-f] <file>]
        [-test -[defsz] <path>]
        [-text [-ignoreCrc] <src> ...]
        [-touchz <path> ...]
        [-truncate [-w] <length> <path> ...]
        [-usage [cmd ...]]

Generic options supported are
-conf <configuration file>     specify an application configuration file
-D <property=value>            use value for given property
-fs <local|namenode:port>      specify a namenode
-jt <local|resourcemanager:port>    specify a ResourceManager
-files <comma separated list of files>    specify comma separated files to be copied to the map reduce cluster
-libjars <comma separated list of jars>    specify comma separated jar files to include in the classpath.
-archives <comma separated list of archives>    specify comma separated archives to be unarchived on the compute machines.

The general command line syntax is
bin/hadoop command [genericOptions] [commandOptions]

#### conlusion : pas de différence

#### question 2: la version de hadoop
 hadoop version
Hadoop 2.7.3.2.6.5.0-292
Subversion git@github.com:hortonworks/hadoop.git -r 3091053c59a62c82d82c9f778c48bde5ef0a89a1
Compiled by jenkins on 2018-05-11T07:53Z
Compiled with protoc 2.5.0
From source with checksum abed71da5bc89062f6f6711179f2058
This command was run using /usr/hdp/2.6.5.0-292/hadoop/hadoop-common-2.7.3.2.6.5.0-292.jar

## 3.2 Importer est exportxer les données
### question 1 : lister l'ensemble des fichiers du repertoire HDFS
#### requete
[maria_dev@sandbox-hdp ~]$ hdfs dfs -ls
#### resultat : ne renvoie rien

### question 2 : afficher ce qu'il y a à la racine de HDFS
[maria_dev@sandbox-hdp ~]$ hdfs dfs -ls /
 hdfs dfs -ls /
Found 11 items
drwxrwxrwx   - yarn   hadoop          0 2018-06-18 15:18 /app-logs
drwxr-xr-x   - hdfs   hdfs            0 2018-06-18 16:13 /apps
drwxr-xr-x   - yarn   hadoop          0 2018-06-18 14:52 /ats
drwxr-xr-x   - hdfs   hdfs            0 2018-06-18 14:52 /hdp
drwx------   - livy   hdfs            0 2018-06-18 15:11 /livy2-recovery
drwxr-xr-x   - mapred hdfs            0 2018-06-18 14:52 /mapred
drwxrwxrwx   - mapred hadoop          0 2018-06-18 14:52 /mr-history
drwxr-xr-x   - hdfs   hdfs            0 2018-06-18 15:59 /ranger
drwxrwxrwx   - spark  hadoop          0 2024-03-26 13:18 /spark2-history
drwxrwxrwx   - hdfs   hdfs            0 2018-06-18 16:06 /tmp
drwxr-xr-x   - hdfs   hdfs            0 2018-06-18 16:08 /user

### question 3 : quelle est la commande pour lire le contenue de user
 hdfs dfs -ls /user
Found 15 items
drwxr-xr-x   - admin     hdfs            0 2018-06-18 14:52 /user/admin
drwxrwx---   - ambari-qa hdfs            0 2018-06-18 14:52 /user/ambari-qa
drwxr-xr-x   - amy_ds    hdfs            0 2018-06-18 14:53 /user/amy_ds
drwxr-xr-x   - root      hdfs            0 2018-06-18 14:52 /user/anonymous
drwxr-xr-x   - druid     hadoop          0 2018-06-18 16:06 /user/druid
drwxr-xr-x   - hbase     hdfs            0 2018-06-18 15:08 /user/hbase
drwxr-xr-x   - hcat      hdfs            0 2018-06-18 15:12 /user/hcat
drwxr-xr-x   - hive      hdfs            0 2018-06-18 15:18 /user/hive
drwxrwxr-x   - livy      hdfs            0 2018-06-18 15:11 /user/livy
drwxr-xr-x   - maria_dev hdfs            0 2018-06-18 14:52 /user/maria_dev
drwxrwxr-x   - oozie     hdfs            0 2018-06-18 16:08 /user/oozie
drwxr-xr-x   - raj_ops   hdfs            0 2018-06-18 14:53 /user/raj_ops
drwxr-xr-x   - root      hdfs            0 2018-06-18 14:52 /user/root
drwxrwxr-x   - spark     hdfs            0 2018-06-18 15:10 /user/spark
drwxr-xr-x   - zeppelin  hdfs            0 2018-06-18 15:10 /user/zeppelin

### question 4 : que ce passe-t-il si on refait avec hadoop fs 
aucune différence

### question 5 : créer le fichier
touch monfichier.txt

### vérification de la question 5 : regarder que le fichier est bien là 
ls

### question 5 bis : modifier le fichier
hadoop fs -appendToFile - monfichier.txt
Vous pouvez ensuite écrire directement dans le terminal de commandes ce que vous voulez mettre dans le fichier

### question 6 : Copiez ce fichier sur HDFS par hdfs dfs -put monfichier.txt. Utilisez hdfs dfs -ls -R pour vérifier.
[maria_dev@sandbox-hdp ~]$ hdfs dfs -put monfichier.txt
put: `monfichier.txt': File exists

### vérification du bon fonctionnement de la question 6
hdfs dfs -ls -R
-rw-r--r--   1 maria_dev hdfs         19 2024-03-26 13:37 monfichier.txt

### question 7 : Si vous voulez envoyer vos données vers HDFS sans garder une copie en local :
hdfs dfs -put /chemin/local/monfichier.txt /chemin/destination/sur/hdfs/

## 3.3 Manipulation des données dans HDFS
### question 1 : afficher le contenue du fichier
hdfs dfs -cat monfichiertxtx

### question 2 : supprimer le fichier
hdfs dfs -rm monfichier.txt

### question 3 : crer des repertoires : requetes exemple
hdfs dfs -mkdir CHEMIN1 CHEMIN2 … 

### question 4 : Créez localement un dossier nommé data et envoyez-le sur HDFS
mkdir data
hdfs dfs -put data /chemin/destination/sur/hdfs/

### question 5 : Copiez le fichier monfichier.txt dans le répertoire data à l’aide de la commande -cp
cp monfichier.txt data/

### question 6 :créer le sous dossier dataset dans data
mkdir data/datasets

 ### question 6 bis : puis déplacez monfichier.txt dans datasets à l’aide de la commande -mv, décrivez vos commandes.
 mv data/monfichier.txt data/datasets/

 ### question 7 :Créer une copie de monfichier.txt dans le répertoire data sous le nom copiedemonfichier.txt.
 cp data/datases/monfichier.txt data/copiedemonfichier.txt

### question 7 bis : Avant de lancer cette commande, il faut vérifier que l’espace local disponible est suffisant pour recevoir les données HDFS, décrivez vos commandes.
#### requete :
 df -h
#### resultat :
Filesystem      Size  Used Avail Use% Mounted on
overlay         107G   24G   79G  23% /
tmpfs            64M     0   64M   0% /dev
/dev/sda3       107G   24G   79G  23% /etc/hosts
shm              64M   12K   64M   1% /dev/shm
tmpfs           3.9G   19M  3.9G   1% /run
tmpfs           798M     0  798M   0% /run/user/1002
tmpfs           798M     0  798M   0% /run/user/1023
tmpfs           798M     0  798M   0% /run/user/1000
tmpfs           798M     0  798M   0% /run/user/1020
tmpfs           798M     0  798M   0% /run/user/1001
tmpfs           798M     0  798M   0% /run/user/1003
tmpfs           798M     0  798M   0% /run/user/1004
tmpfs           798M     0  798M   0% /run/user/1008
tmpfs           798M     0  798M   0% /run/user/1026
tmpfs           798M     0  798M   0% /run/user/1012
tmpfs           798M     0  798M   0% /run/user/1010
tmpfs           798M     0  798M   0% /run/user/1011
tmpfs           798M     0  798M   0% /run/user/1015
tmpfs           798M     0  798M   0% /run/user/1005
#### conclusion : partout il reste beaucoup de place pour le stockage

### question 8 :Si on veut supprimer un répertoire depuis le système de fichiers HDFS
hdfs dfs -rm -r /chemin/du/repertoire

### question  9 :Une commande qui vous permet de voir « l’état de santé » de votre HDFS (elle vérifie les incohérences : blocks manquants, nom de réplicas insufusants,…) : hdfs fsck /user
#### requetes:
hdfs fsck /user
#### resultat
Connecting to namenode via http://sandbox-hdp.hortonworks.com:50070/fsck?ugi=maria_dev&path=%2Fuser
FSCK started by maria_dev (auth:SIMPLE) from /172.18.0.2 for path /user at Tue Mar 26 14:58:48 UTC 2024
....................................................................................................
....................................................................................................
....................................................................................................
....................................................................................................
....................................................................................................
....................................................................................................
....................................................................................................
....................................................................................................
....................................................................................................
............................................................................................Status: HEALTHY
 Total size:    976496354 B
 Total dirs:    44
 Total files:   992
 Total symlinks:                0
 Total blocks (validated):      993 (avg. block size 983380 B)
 Minimally replicated blocks:   993 (100.0 %)
 Over-replicated blocks:        0 (0.0 %)
 Under-replicated blocks:       0 (0.0 %)
 Mis-replicated blocks:         0 (0.0 %)
 Default replication factor:    1
 Average block replication:     1.0
 Corrupt blocks:                0
 Missing replicas:              0 (0.0 %)
 Number of data-nodes:          1
 Number of racks:               1
FSCK ended at Tue Mar 26 14:58:48 UTC 2024 in 238 milliseconds


The filesystem under path '/user' is HEALTHY
#### explication du résultat
tout est normal, statut HEALTHY

## 3.4 Manipulation de fichiers télécharger depuis un serveur
### question 1 : a partir de la vm télécharger les données
#### requete
wget
#### resultat
wget: missing URL
Usage: wget [OPTION]... [URL]...

Try `wget --help' for more options.
#### résolution de l'erreur
rajouter l'url dans la requetes
wget https://files.grouplens.org/datasets/movielens/ml-1m.zip
--2024-03-26 15:37:00--  https://files.grouplens.org/datasets/movielens/ml-1m.zip
Resolving files.grouplens.org (files.grouplens.org)... 128.101.65.152
Connecting to files.grouplens.org (files.grouplens.org)|128.101.65.152|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 5917549 (5.6M) [application/zip]
Saving to: ‘ml-1m.zip’

100%[==============================================================================>] 5,917,549   1.53MB/s   in 3.7s

2024-03-26 15:37:05 (1.53 MB/s) - ‘ml-1m.zip’ saved [5917549/5917549]

### question 2 : décompressez le fichier
#### en local
unzip ml-1m.zip
Archive:  ml-1m.zip
   creating: ml-1m/
  inflating: ml-1m/movies.dat
  inflating: ml-1m/ratings.dat
  inflating: ml-1m/README
  inflating: ml-1m/users.dat
#### sur hdfs
hdfs dfs -mkdir -p /data_zip
hdfs dfs -mkdir -p /new_data
hdfs dfs -put ml-1m.zip /data_zip/ml-1m_copie.zip
hadoop fs -unzip /data_zip/ml-1m_copie.zip new_data/ml-1m
la première commande sert à mettre le fichier sur hdfs et la deuxième sert à dzipper le fichier

### question 3 : créez un repertoire datasets/movies en local et sur hdfs
mkdir -p datasets/movies
hdfs dfs -mkdir -p /datasets/movies

### question 4 : Déroulez les étapes de création des deux dossier /datasets/movies et la copie du fichier rating.dat à partir du système local vers HDFS (dans movies).
la création des deux dossier datasets et movies on été créée à la question 3 et concernant la copie du fichier 
hdfs dfs -put ml-1m/ratings.dat  /datasets/movies/ratings_copie.dat

### question 4 bis : afficher combien de blocs occupe le fichier 
#### requete :
hdfs fsck /datasets/movies/ratings_copie.dat -files -blocks
#### résultat :
Connecting to namenode via http://sandbox-hdp.hortonworks.com:50070/fsck?ugi=maria_dev&files=1&blocks=1&path=%2Fdatasets%2Fmovies%2Fratings_copie.dat
FSCK started by maria_dev (auth:SIMPLE) from /172.18.0.2 for path /datasets/movies/ratings_copie.dat at Tue Mar 26 16:08:34 UTC 2024
/datasets/movies/ratings_copie.dat 24594131 bytes, 1 block(s):  OK
0. BP-243674277-172.17.0.2-1529333510191:blk_1073743046_2226 len=24594131 repl=1

Status: HEALTHY
 Total size:    24594131 B
 Total dirs:    0
 Total files:   1
 Total symlinks:                0
 Total blocks (validated):      1 (avg. block size 24594131 B)
 Minimally replicated blocks:   1 (100.0 %)
 Over-replicated blocks:        0 (0.0 %)
 Under-replicated blocks:       0 (0.0 %)
 Mis-replicated blocks:         0 (0.0 %)
 Default replication factor:    1
 Average block replication:     1.0
 Corrupt blocks:                0
 Missing replicas:              0 (0.0 %)
 Number of data-nodes:          1
 Number of racks:               1
FSCK ended at Tue Mar 26 16:08:34 UTC 2024 in 2 milliseconds


The filesystem under path '/datasets/movies/ratings_copie.dat' is HEALTHY*
#### explication du résultat :
ce rapport indique que le fichier "ratings_copie.dat" dans le répertoire "/datasets/movies/" est en bon état, avec une taille, une réplication et une intégrité correctes. il occupe 1 seul bloc 

### question 5 : recuperer le deuxième fichier zip 
wget https://files.grouplens.org/datasets/movielens/ml-25m.zip*
#### resultat :
[maria_dev@sandbox-hdp ~]$ wget https://files.grouplens.org/datasets/movielens/ml-25m.zip
--2024-03-28 09:53:40--  https://files.grouplens.org/datasets/movielens/ml-25m.zip
Resolving files.grouplens.org (files.grouplens.org)... 128.101.65.152
Connecting to files.grouplens.org (files.grouplens.org)|128.101.65.152|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 261978986 (250M) [application/zip]
Saving to: ‘ml-25m.zip’

100%[==============================================================================>] 261,978,986 10.1MB/s   in 46s

2024-03-28 09:54:27 (5.38 MB/s) - ‘ml-25m.zip’ saved [261978986/261978986]

### question 6 : Décompressez-le puis copiez le fichier ratings.csv dans un autre répertoire dans HDFS et trouver le nombre de blocs occupé par ce dernier.
#### dézipper et mettre sur hdfs
hdfs dfs -mkdir -p /new_data_2
hdfs dfs -put ml-25m.zip /data_zip/ml-25m_copie.zip
hadoop fs -unzip /data_zip/ml-25m_copie.zip new_data_2/ml-25m/ratings.csv
unzip ml-25m.zip
Archive:  ml-25m.zip
   creating: ml-25m/
  inflating: ml-25m/tags.csv
  inflating: ml-25m/links.csv
  inflating: ml-25m/README.txt
  inflating: ml-25m/ratings.csv

#### nombre de bloc qu'occupe ce dernier 
hdfs fsck /new_data_2/ml-25m/ratings.csv -files -blocks
##### resultat :
[maria_dev@sandbox-hdp ~]$ hdfs fsck /user/maria_dev/new_data/ratings.csv -files -blocks
Connecting to namenode via http://sandbox-hdp.hortonworks.com:50070/fsck?ugi=maria_dev&files=1&blocks=1&path=%2Fuser%2Fmaria_dev%2Fnew_data%2Fratings.csv
FSCK started by maria_dev (auth:SIMPLE) from /172.18.0.2 for path /user/maria_dev/new_data/ratings.csv at Thu Mar 28 10:21:08 UTC 2024
/user/maria_dev/new_data/ratings.csv 678260987 bytes, 6 block(s):  OK
0. BP-243674277-172.17.0.2-1529333510191:blk_1073743064_2248 len=134217728 repl=1
1. BP-243674277-172.17.0.2-1529333510191:blk_1073743065_2249 len=134217728 repl=1
2. BP-243674277-172.17.0.2-1529333510191:blk_1073743066_2250 len=134217728 repl=1
3. BP-243674277-172.17.0.2-1529333510191:blk_1073743067_2251 len=134217728 repl=1
4. BP-243674277-172.17.0.2-1529333510191:blk_1073743068_2252 len=134217728 repl=1
5. BP-243674277-172.17.0.2-1529333510191:blk_1073743069_2253 len=7172347 repl=1

Status: HEALTHY
 Total size:    678260987 B
 Total dirs:    0
 Total files:   1
 Total symlinks:                0
 Total blocks (validated):      6 (avg. block size 113043497 B)
 Minimally replicated blocks:   6 (100.0 %)
 Over-replicated blocks:        0 (0.0 %)
 Under-replicated blocks:       0 (0.0 %)
 Mis-replicated blocks:         0 (0.0 %)
 Default replication factor:    1
 Average block replication:     1.0
 Corrupt blocks:                0
 Missing replicas:              0 (0.0 %)
 Number of data-nodes:          1
 Number of racks:               1
FSCK ended at Thu Mar 28 10:21:08 UTC 2024 in 1 milliseconds


The filesystem under path '/user/maria_dev/new_data/ratings.csv' is HEALTHY
##### explication : il occupe 6 blocks

## 3.5 Fichier de configuratgion HDFS
### question 1 : Consultez le contenu de ce fichier
hdfs getconf -confkey dfs.replication

### question 2 : Quelle est la taille du bloc sur votre HDFS ?
hdfs getconf -confKey dfs.blocksize
### changer la taille du bloc 
hdfs dfs -D dfs.blocksize=67108864 -put Monfichier

### question 3 : Vérifiez en envoyant un fichier sur HDFS et commenter votre analyse. (hint: Je vous demande de faire les manipulations pour voir le nombres des blocs)
#### Étape 1 : Crer le fichier 
touch test.txt
hadoop fs -appendToFile - test.txt 
#### Étape 2 : Envoyer un fichier sur HDFS
hdfs dfs -put test.txt data/test.txt
#### Étape 3 : Examiner le rapport FSCK
hdfs fsck data/test.txt -files -blocks -locations
#### explication :
Cette commande affichera un rapport FSCK détaillé pour le fichier spécifié, y compris le nombre de blocs utilisés par le fichier.
En examinant le rapport FSCK, nous pourrons voir le nombre de blocs utilisés par le fichier ainsi que d'autres informations pertinentes telles que la réplication, l'état des blocs, etc.
En commentant cette analyse, nous pouvons discuter du nombre de blocs utilisés par le fichier par rapport à la taille du fichier et à la taille du bloc configurée sur HDFS. Cela nous aidera à comprendre comment HDFS gère le stockage des fichiers en les décomposant en blocs de taille fixe et en répartissant ces blocs sur différents nœuds du cluster.

# 4. Hadoop
## 4.1. Préparation de la vm (MrJob, Python ...)
### 4.1.1. Mise à jour de la SandBox HDP
#### commande 1
##### requete
yum-config-manager --save --setopt=HDP-SOLR-2.6-100.skip_if_unavailable=true
##### résultat
Loaded plugins: fastestmirror, ovl
ovl: Error while doing RPMdb copy-up:
[Errno 13] Permission denied: '/var/lib/rpm/.dbenv.lock'
You must be root to change the yum configuration.
#### commande 2
###### requete
yum install https://repo.ius.io/ius-release-el7.rpm https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
##### résultat
Loaded plugins: fastestmirror, ovl
ovl: Error while doing RPMdb copy-up:
[Errno 13] Permission denied: '/var/lib/rpm/.dbenv.lock'
You need to be root to perform this command.
##### Pour les deux commandes une erreur concernant la permission
##### en changeant de compte (passant administrateur)
###### commande
sudo su root
###### resultat
on passe de "[maria_dev@sandbox-hdp ~]$" à ça "[root@sandbox-hdp maria_dev]#"
###### pour la première commande
Loaded plugins: fastestmirror, ovl
========================================================= main =========================================================
[main]
alwaysprompt = True
assumeno = False
assumeyes = False
autocheck_running_kernel = True
autosavets = True
bandwidth = 0
bugtracker_url = http://bugs.centos.org/set_project.php?project_id=23&ref=http://bugs.centos.org/bug_report_page.php?category=yum
cache = 0
cachedir = /var/cache/yum/x86_64/7
check_config_file_age = True
clean_requirements_on_remove = False
color = auto
color_list_available_downgrade = dim,cyan
color_list_available_install = normal
color_list_available_reinstall = bold,underline,green
color_list_available_running_kernel = bold,underline
color_list_available_upgrade = bold,blue
color_list_installed_extra = bold,red
color_list_installed_newer = bold,yellow
color_list_installed_older = bold
color_list_installed_reinstall = normal
color_list_installed_running_kernel = bold,underline
color_search_match = bold
color_update_installed = normal
color_update_local = bold
color_update_remote = normal
commands =
debuglevel = 2
deltarpm = 2
deltarpm_metadata_percentage = 100
deltarpm_percentage = 75
depsolve_loop_limit = 100
disable_includes =
diskspacecheck = True
distroverpkg = centos-release
downloaddir =
downloadonly =
enable_group_conditionals = True
enabled = True
enablegroups = True
errorlevel = 2
exactarch = True
exactarchlist =
exclude =
exit_on_lock = False
failovermethod = priority
fssnap_abort_on_errors = any
fssnap_automatic_keep = 1
fssnap_automatic_post = False
fssnap_automatic_pre = False
fssnap_devices = !*/swap,
   !*/lv_swap
fssnap_percentage = 100
ftp_disable_epsv = False
gaftonmode = False
gpgcheck = True
group_command = objects
group_package_types = mandatory,
   default
groupremove_leaf_only = False
history_list_view = single-user-commands
history_record = True
history_record_packages = yum,
   rpm
http_caching = all
installonly_limit = 5
installonlypkgs = kernel,
   kernel-bigmem,
   installonlypkg(kernel-module),
   installonlypkg(vm),
   kernel-enterprise,
   kernel-smp,
   kernel-debug,
   kernel-unsupported,
   kernel-source,
   kernel-devel,
   kernel-PAE,
   kernel-PAE-debug
installroot = /
ip_resolve =
keepalive = True
keepcache = False
kernelpkgnames = kernel,
   kernel-smp,
   kernel-enterprise,
   kernel-bigmem,
   kernel-BOOT,
   kernel-PAE,
   kernel-PAE-debug
loadts_ignoremissing = False
loadts_ignorenewrpm = False
loadts_ignorerpm = False
localpkg_gpgcheck = False
logfile = /var/log/yum.log
max_connections = 0
mddownloadpolicy = sqlite
mdpolicy = group:small
metadata_expire = 21600
metadata_expire_filter = read-only:present
minrate = 0
mirrorlist_expire = 86400
multilib_policy = best
obsoletes = True
override_install_langs = en_US.utf8
overwrite_groups = False
password =
payload_gpgcheck = False
persistdir = /var/lib/yum
pluginconfpath = /etc/yum/pluginconf.d
pluginpath = /usr/share/yum-plugins,
   /usr/lib/yum-plugins
plugins = True
progess_obj =
protected_multilib = True
protected_packages = yum,
   systemd
proxy = False
proxy_password =
proxy_username =
query_install_excludes = False
recent = 7
recheck_installed_requires = True
remove_leaf_only = False
repo_gpgcheck = False
repopkgsremove_leaf_only = False
reposdir = /etc/yum/repos.d,
   /etc/yum.repos.d
reset_nice = True
retries = 10
rpm_check_debug = True
rpmverbosity = info
showdupesfromrepos = False
skip_broken = False
skip_missing_names_on_install = True
skip_missing_names_on_update = True
ssl_check_cert_permissions = True
sslcacert =
sslclientcert =
sslclientkey =
sslverify = True
syslog_device = /dev/log
syslog_facility = LOG_USER
syslog_ident =
throttle = 0
timeout = 30.0
tolerant = True
tsflags = nodocs
ui_repoid_vars = releasever,
   basearch
upgrade_group_objects_upgrade = True
upgrade_requirements_on_install = False
username =
usr_w_check = True

================================================= repo: HDP-2.6-repo-1 =================================================
[HDP-2.6-repo-1]
async = True
bandwidth = 0
base_persistdir = /var/lib/yum/repos/x86_64/7
baseurl = http://public-repo-1.hortonworks.com/HDP/centos7/2.x/updates/2.6.5.0
cache = 0
cachedir = /var/cache/yum/x86_64/7/HDP-2.6-repo-1
check_config_file_age = True
compare_providers_priority = 80
cost = 1000
deltarpm_metadata_percentage = 100
deltarpm_percentage =
enabled = True
enablegroups = True
exclude =
failovermethod = priority
ftp_disable_epsv = False
gpgcadir = /var/lib/yum/repos/x86_64/7/HDP-2.6-repo-1/gpgcadir
gpgcakey =
gpgcheck = False
gpgdir = /var/lib/yum/repos/x86_64/7/HDP-2.6-repo-1/gpgdir
gpgkey =
hdrdir = /var/cache/yum/x86_64/7/HDP-2.6-repo-1/headers
http_caching = all
includepkgs =
ip_resolve =
keepalive = True
keepcache = False
mddownloadpolicy = sqlite
mdpolicy = group:small
mediaid =
metadata_expire = 21600
metadata_expire_filter = read-only:present
metalink =
minrate = 0
mirrorlist =
mirrorlist_expire = 86400
name = HDP-2.6-repo-1
old_base_cache_dir =
password =
persistdir = /var/lib/yum/repos/x86_64/7/HDP-2.6-repo-1
pkgdir = /var/cache/yum/x86_64/7/HDP-2.6-repo-1/packages
proxy = False
proxy_dict =
proxy_password =
proxy_username =
repo_gpgcheck = False
retries = 10
skip_if_unavailable = False
ssl_check_cert_permissions = True
sslcacert =
sslclientcert =
sslclientkey =
sslverify = True
throttle = 0
timeout = 30.0
ui_id = HDP-2.6-repo-1
ui_repoid_vars = releasever,
   basearch
username =

================================================ repo: HDP-SOLR-2.6-100 ================================================
[HDP-SOLR-2.6-100]
async = True
bandwidth = 0
base_persistdir = /var/lib/yum/repos/x86_64/7
baseurl = http://public-repo-1.hortonworks.com/HDP-SOLR-2.6-100/repos/centos7
cache = 0
cachedir = /var/cache/yum/x86_64/7/HDP-SOLR-2.6-100
check_config_file_age = True
compare_providers_priority = 80
cost = 1000
deltarpm_metadata_percentage = 100
deltarpm_percentage =
enabled = True
enablegroups = True
exclude =
failovermethod = priority
ftp_disable_epsv = False
gpgcadir = /var/lib/yum/repos/x86_64/7/HDP-SOLR-2.6-100/gpgcadir
gpgcakey =
gpgcheck = False
gpgdir = /var/lib/yum/repos/x86_64/7/HDP-SOLR-2.6-100/gpgdir
gpgkey = http://public-repo-1.hortonworks.com/HDP-SOLR-2.6-100/repos/centos7/RPM-GPG-KEY/RPM-GPG-KEY-Jenkins
hdrdir = /var/cache/yum/x86_64/7/HDP-SOLR-2.6-100/headers
http_caching = all
includepkgs =
ip_resolve =
keepalive = True
keepcache = False
mddownloadpolicy = sqlite
mdpolicy = group:small
mediaid =
metadata_expire = 21600
metadata_expire_filter = read-only:present
metalink =
minrate = 0
mirrorlist =
mirrorlist_expire = 86400
name = Hortonworks Data Platform Version - HDP-SOLR-2.6-100
old_base_cache_dir =
password =
persistdir = /var/lib/yum/repos/x86_64/7/HDP-SOLR-2.6-100
pkgdir = /var/cache/yum/x86_64/7/HDP-SOLR-2.6-100/packages
proxy = False
proxy_dict =
proxy_password =
proxy_username =
repo_gpgcheck = False
retries = 10
skip_if_unavailable = True
ssl_check_cert_permissions = True
sslcacert =
sslclientcert =
sslclientkey =
sslverify = True
throttle = 0
timeout = 30.0
ui_id = HDP-SOLR-2.6-100
ui_repoid_vars = releasever,
   basearch
username =

=========================================== repo: HDP-UTILS-1.1.0.22-repo-1 ============================================
[HDP-UTILS-1.1.0.22-repo-1]
async = True
bandwidth = 0
base_persistdir = /var/lib/yum/repos/x86_64/7
baseurl = http://public-repo-1.hortonworks.com/HDP-UTILS-1.1.0.22/repos/centos7
cache = 0
cachedir = /var/cache/yum/x86_64/7/HDP-UTILS-1.1.0.22-repo-1
check_config_file_age = True
compare_providers_priority = 80
cost = 1000
deltarpm_metadata_percentage = 100
deltarpm_percentage =
enabled = True
enablegroups = True
exclude =
failovermethod = priority
ftp_disable_epsv = False
gpgcadir = /var/lib/yum/repos/x86_64/7/HDP-UTILS-1.1.0.22-repo-1/gpgcadir
gpgcakey =
gpgcheck = False
gpgdir = /var/lib/yum/repos/x86_64/7/HDP-UTILS-1.1.0.22-repo-1/gpgdir
gpgkey =
hdrdir = /var/cache/yum/x86_64/7/HDP-UTILS-1.1.0.22-repo-1/headers
http_caching = all
includepkgs =
ip_resolve =
keepalive = True
keepcache = False
mddownloadpolicy = sqlite
mdpolicy = group:small
mediaid =
metadata_expire = 21600
metadata_expire_filter = read-only:present
metalink =
minrate = 0
mirrorlist =
mirrorlist_expire = 86400
name = HDP-UTILS-1.1.0.22-repo-1
old_base_cache_dir =
password =
persistdir = /var/lib/yum/repos/x86_64/7/HDP-UTILS-1.1.0.22-repo-1
pkgdir = /var/cache/yum/x86_64/7/HDP-UTILS-1.1.0.22-repo-1/packages
proxy = False
proxy_dict =
proxy_password =
proxy_username =
repo_gpgcheck = False
retries = 10
skip_if_unavailable = False
ssl_check_cert_permissions = True
sslcacert =
sslclientcert =
sslclientkey =
sslverify = True
throttle = 0
timeout = 30.0
ui_id = HDP-UTILS-1.1.0.22-repo-1
ui_repoid_vars = releasever,
   basearch
username =

================================================= repo: ambari-2.6.2.0 =================================================
[ambari-2.6.2.0]
async = True
bandwidth = 0
base_persistdir = /var/lib/yum/repos/x86_64/7
baseurl = http://public-repo-1.hortonworks.com/ambari/centos7/2.x/updates/2.6.2.0
cache = 0
cachedir = /var/cache/yum/x86_64/7/ambari-2.6.2.0
check_config_file_age = True
compare_providers_priority = 80
cost = 1000
deltarpm_metadata_percentage = 100
deltarpm_percentage =
enabled = True
enablegroups = True
exclude =
failovermethod = priority
ftp_disable_epsv = False
gpgcadir = /var/lib/yum/repos/x86_64/7/ambari-2.6.2.0/gpgcadir
gpgcakey =
gpgcheck = True
gpgdir = /var/lib/yum/repos/x86_64/7/ambari-2.6.2.0/gpgdir
gpgkey = http://public-repo-1.hortonworks.com/ambari/centos7/2.x/updates/2.6.2.0/RPM-GPG-KEY/RPM-GPG-KEY-Jenkins
hdrdir = /var/cache/yum/x86_64/7/ambari-2.6.2.0/headers
http_caching = all
includepkgs =
ip_resolve =
keepalive = True
keepcache = False
mddownloadpolicy = sqlite
mdpolicy = group:small
mediaid =
metadata_expire = 21600
metadata_expire_filter = read-only:present
metalink =
minrate = 0
mirrorlist =
mirrorlist_expire = 86400
name = ambari Version - ambari-2.6.2.0
old_base_cache_dir =
password =
persistdir = /var/lib/yum/repos/x86_64/7/ambari-2.6.2.0
pkgdir = /var/cache/yum/x86_64/7/ambari-2.6.2.0/packages
proxy = False
proxy_dict =
proxy_password =
proxy_username =
repo_gpgcheck = False
retries = 10
skip_if_unavailable = False
ssl_check_cert_permissions = True
sslcacert =
sslclientcert =
sslclientkey =
sslverify = True
throttle = 0
timeout = 30.0
ui_id = ambari-2.6.2.0
ui_repoid_vars = releasever,
   basearch
username =

====================================================== repo: base ======================================================
[base]
async = True
bandwidth = 0
base_persistdir = /var/lib/yum/repos/x86_64/7
baseurl =
cache = 0
cachedir = /var/cache/yum/x86_64/7/base
check_config_file_age = True
compare_providers_priority = 80
cost = 1000
deltarpm_metadata_percentage = 100
deltarpm_percentage =
enabled = True
enablegroups = True
exclude =
failovermethod = priority
ftp_disable_epsv = False
gpgcadir = /var/lib/yum/repos/x86_64/7/base/gpgcadir
gpgcakey =
gpgcheck = True
gpgdir = /var/lib/yum/repos/x86_64/7/base/gpgdir
gpgkey = file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7
hdrdir = /var/cache/yum/x86_64/7/base/headers
http_caching = all
includepkgs =
ip_resolve =
keepalive = True
keepcache = False
mddownloadpolicy = sqlite
mdpolicy = group:small
mediaid =
metadata_expire = 21600
metadata_expire_filter = read-only:present
metalink =
minrate = 0
mirrorlist = http://mirrorlist.centos.org/?release=7&arch=x86_64&repo=os&infra=container
mirrorlist_expire = 86400
name = CentOS-7 - Base
old_base_cache_dir =
password =
persistdir = /var/lib/yum/repos/x86_64/7/base
pkgdir = /var/cache/yum/x86_64/7/base/packages
proxy = False
proxy_dict =
proxy_password =
proxy_username =
repo_gpgcheck = False
retries = 10
skip_if_unavailable = False
ssl_check_cert_permissions = True
sslcacert =
sslclientcert =
sslclientkey =
sslverify = True
throttle = 0
timeout = 30.0
ui_id = base/7/x86_64
ui_repoid_vars = releasever,
   basearch
username =

====================================================== repo: epel ======================================================
[epel]
async = True
bandwidth = 0
base_persistdir = /var/lib/yum/repos/x86_64/7
baseurl =
cache = 0
cachedir = /var/cache/yum/x86_64/7/epel
check_config_file_age = True
compare_providers_priority = 80
cost = 1000
deltarpm_metadata_percentage = 100
deltarpm_percentage =
enabled = True
enablegroups = True
exclude =
failovermethod = priority
ftp_disable_epsv = False
gpgcadir = /var/lib/yum/repos/x86_64/7/epel/gpgcadir
gpgcakey =
gpgcheck = True
gpgdir = /var/lib/yum/repos/x86_64/7/epel/gpgdir
gpgkey = file:///etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7
hdrdir = /var/cache/yum/x86_64/7/epel/headers
http_caching = all
includepkgs =
ip_resolve =
keepalive = True
keepcache = False
mddownloadpolicy = sqlite
mdpolicy = group:small
mediaid =
metadata_expire = 21600
metadata_expire_filter = read-only:present
metalink = https://mirrors.fedoraproject.org/metalink?repo=epel-7&arch=x86_64
minrate = 0
mirrorlist =
mirrorlist_expire = 86400
name = Extra Packages for Enterprise Linux 7 - x86_64
old_base_cache_dir =
password =
persistdir = /var/lib/yum/repos/x86_64/7/epel
pkgdir = /var/cache/yum/x86_64/7/epel/packages
proxy = False
proxy_dict =
proxy_password =
proxy_username =
repo_gpgcheck = False
retries = 10
skip_if_unavailable = False
ssl_check_cert_permissions = True
sslcacert =
sslclientcert =
sslclientkey =
sslverify = True
throttle = 0
timeout = 30.0
ui_id = epel/x86_64
ui_repoid_vars = releasever,
   basearch
username =

===================================================== repo: extras =====================================================
[extras]
async = True
bandwidth = 0
base_persistdir = /var/lib/yum/repos/x86_64/7
baseurl =
cache = 0
cachedir = /var/cache/yum/x86_64/7/extras
check_config_file_age = True
compare_providers_priority = 80
cost = 1000
deltarpm_metadata_percentage = 100
deltarpm_percentage =
enabled = True
enablegroups = True
exclude =
failovermethod = priority
ftp_disable_epsv = False
gpgcadir = /var/lib/yum/repos/x86_64/7/extras/gpgcadir
gpgcakey =
gpgcheck = True
gpgdir = /var/lib/yum/repos/x86_64/7/extras/gpgdir
gpgkey = file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7
hdrdir = /var/cache/yum/x86_64/7/extras/headers
http_caching = all
includepkgs =
ip_resolve =
keepalive = True
keepcache = False
mddownloadpolicy = sqlite
mdpolicy = group:small
mediaid =
metadata_expire = 21600
metadata_expire_filter = read-only:present
metalink =
minrate = 0
mirrorlist = http://mirrorlist.centos.org/?release=7&arch=x86_64&repo=extras&infra=container
mirrorlist_expire = 86400
name = CentOS-7 - Extras
old_base_cache_dir =
password =
persistdir = /var/lib/yum/repos/x86_64/7/extras
pkgdir = /var/cache/yum/x86_64/7/extras/packages
proxy = False
proxy_dict =
proxy_password =
proxy_username =
repo_gpgcheck = False
retries = 10
skip_if_unavailable = False
ssl_check_cert_permissions = True
sslcacert =
sslclientcert =
sslclientkey =
sslverify = True
throttle = 0
timeout = 30.0
ui_id = extras/7/x86_64
ui_repoid_vars = releasever,
   basearch
username =

====================================================== repo: ius =======================================================
[ius]
async = True
bandwidth = 0
base_persistdir = /var/lib/yum/repos/x86_64/7
baseurl =
cache = 0
cachedir = /var/cache/yum/x86_64/7/ius
check_config_file_age = True
compare_providers_priority = 80
cost = 1000
deltarpm_metadata_percentage = 100
deltarpm_percentage =
enabled = True
enablegroups = True
exclude =
failovermethod = priority
ftp_disable_epsv = False
gpgcadir = /var/lib/yum/repos/x86_64/7/ius/gpgcadir
gpgcakey =
gpgcheck = True
gpgdir = /var/lib/yum/repos/x86_64/7/ius/gpgdir
gpgkey = file:///etc/pki/rpm-gpg/IUS-COMMUNITY-GPG-KEY
hdrdir = /var/cache/yum/x86_64/7/ius/headers
http_caching = all
includepkgs =
ip_resolve =
keepalive = True
keepcache = False
mddownloadpolicy = sqlite
mdpolicy = group:small
mediaid =
metadata_expire = 21600
metadata_expire_filter = read-only:present
metalink =
minrate = 0
mirrorlist = https://mirrors.iuscommunity.org/mirrorlist?repo=ius-centos7&arch=x86_64&protocol=http
mirrorlist_expire = 86400
name = IUS Community Packages for Enterprise Linux 7 - x86_64
old_base_cache_dir =
password =
persistdir = /var/lib/yum/repos/x86_64/7/ius
pkgdir = /var/cache/yum/x86_64/7/ius/packages
proxy = False
proxy_dict =
proxy_password =
proxy_username =
repo_gpgcheck = False
retries = 10
skip_if_unavailable = False
ssl_check_cert_permissions = True
sslcacert =
sslclientcert =
sslclientkey =
sslverify = True
throttle = 0
timeout = 30.0
ui_id = ius/x86_64
ui_repoid_vars = releasever,
   basearch
username =

=============================================== repo: mysql57-community ================================================
[mysql57-community]
async = True
bandwidth = 0
base_persistdir = /var/lib/yum/repos/x86_64/7
baseurl = http://repo.mysql.com/yum/mysql-5.7-community/el/7/x86_64/
cache = 0
cachedir = /var/cache/yum/x86_64/7/mysql57-community
check_config_file_age = True
compare_providers_priority = 80
cost = 1000
deltarpm_metadata_percentage = 100
deltarpm_percentage =
enabled = True
enablegroups = True
exclude =
failovermethod = priority
ftp_disable_epsv = False
gpgcadir = /var/lib/yum/repos/x86_64/7/mysql57-community/gpgcadir
gpgcakey =
gpgcheck = True
gpgdir = /var/lib/yum/repos/x86_64/7/mysql57-community/gpgdir
gpgkey = file:///etc/pki/rpm-gpg/RPM-GPG-KEY-mysql
hdrdir = /var/cache/yum/x86_64/7/mysql57-community/headers
http_caching = all
includepkgs =
ip_resolve =
keepalive = True
keepcache = False
mddownloadpolicy = sqlite
mdpolicy = group:small
mediaid =
metadata_expire = 21600
metadata_expire_filter = read-only:present
metalink =
minrate = 0
mirrorlist =
mirrorlist_expire = 86400
name = MySQL 5.7 Community Server
old_base_cache_dir =
password =
persistdir = /var/lib/yum/repos/x86_64/7/mysql57-community
pkgdir = /var/cache/yum/x86_64/7/mysql57-community/packages
proxy = False
proxy_dict =
proxy_password =
proxy_username =
repo_gpgcheck = False
retries = 10
skip_if_unavailable = False
ssl_check_cert_permissions = True
sslcacert =
sslclientcert =
sslclientkey =
sslverify = True
throttle = 0
timeout = 30.0
ui_id = mysql57-community/x86_64
ui_repoid_vars = releasever,
   basearch
username =

==================================================== repo: updates =====================================================
[updates]
async = True
bandwidth = 0
base_persistdir = /var/lib/yum/repos/x86_64/7
baseurl =
cache = 0
cachedir = /var/cache/yum/x86_64/7/updates
check_config_file_age = True
compare_providers_priority = 80
cost = 1000
deltarpm_metadata_percentage = 100
deltarpm_percentage =
enabled = True
enablegroups = True
exclude =
failovermethod = priority
ftp_disable_epsv = False
gpgcadir = /var/lib/yum/repos/x86_64/7/updates/gpgcadir
gpgcakey =
gpgcheck = True
gpgdir = /var/lib/yum/repos/x86_64/7/updates/gpgdir
gpgkey = file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7
hdrdir = /var/cache/yum/x86_64/7/updates/headers
http_caching = all
includepkgs =
ip_resolve =
keepalive = True
keepcache = False
mddownloadpolicy = sqlite
mdpolicy = group:small
mediaid =
metadata_expire = 21600
metadata_expire_filter = read-only:present
metalink =
minrate = 0
mirrorlist = http://mirrorlist.centos.org/?release=7&arch=x86_64&repo=updates&infra=container
mirrorlist_expire = 86400
name = CentOS-7 - Updates
old_base_cache_dir =
password =
persistdir = /var/lib/yum/repos/x86_64/7/updates
pkgdir = /var/cache/yum/x86_64/7/updates/packages
proxy = False
proxy_dict =
proxy_password =
proxy_username =
repo_gpgcheck = False
retries = 10
skip_if_unavailable = False
ssl_check_cert_permissions = True
sslcacert =
sslclientcert =
sslclientkey =
sslverify = True
throttle = 0
timeout = 30.0
ui_id = updates/7/x86_64
ui_repoid_vars = releasever,
   basearch
username =

######  pour la deuxième commande
[maria_dev@sandbox-hdp ~]$ yum install https://repo.ius.io/ius-release-el7.rpm https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
Loaded plugins: fastestmirror, ovl
ovl: Error while doing RPMdb copy-up:
[Errno 13] Permission denied: '/var/lib/rpm/.dbenv.lock'
You need to be root to perform this command.
[maria_dev@sandbox-hdp ~]$ sudo yum install https://repo.ius.io/ius-release-el7.rpm https://dl.fedoraproject.org/pub/epe
l/epel-release-latest-7.noarch.rpm
Loaded plugins: fastestmirror, ovl
ius-release-el7.rpm                                                                              | 8.2 kB  00:00:00
Examining /var/tmp/yum-root-UoIVje/ius-release-el7.rpm: ius-release-2-1.el7.ius.noarch
Marking /var/tmp/yum-root-UoIVje/ius-release-el7.rpm as an update to ius-release-1.0-15.ius.centos7.noarch
epel-release-latest-7.noarch.rpm                                                                 |  15 kB  00:00:00
Examining /var/tmp/yum-root-UoIVje/epel-release-latest-7.noarch.rpm: epel-release-7-14.noarch
Marking /var/tmp/yum-root-UoIVje/epel-release-latest-7.noarch.rpm as an update to epel-release-7-11.noarch
Resolving Dependencies
--> Running transaction check
---> Package epel-release.noarch 0:7-11 will be updated
---> Package epel-release.noarch 0:7-14 will be an update
---> Package ius-release.noarch 0:1.0-15.ius.centos7 will be updated
---> Package ius-release.noarch 0:2-1.el7.ius will be an update
--> Finished Dependency Resolution

Dependencies Resolved

========================================================================================================================
 Package                  Arch               Version                    Repository                                 Size
========================================================================================================================
Updating:
 epel-release             noarch             7-14                       /epel-release-latest-7.noarch              25 k
 ius-release              noarch             2-1.el7.ius                /ius-release-el7                          4.5 k

Transaction Summary
========================================================================================================================
Upgrade  2 Packages

Total size: 30 k
Is this ok [y/d/N]: y
Downloading packages:
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  Updating   : epel-release-7-14.noarch                                                                             1/4
  Updating   : ius-release-2-1.el7.ius.noarch                                                                       2/4
  Cleanup    : ius-release-1.0-15.ius.centos7.noarch                                                                3/4
  Cleanup    : epel-release-7-11.noarch                                                                             4/4
  Verifying  : epel-release-7-14.noarch                                                                             1/4
  Verifying  : ius-release-2-1.el7.ius.noarch                                                                       2/4
  Verifying  : ius-release-1.0-15.ius.centos7.noarch                                                                3/4
  Verifying  : epel-release-7-11.noarch                                                                             4/4

Updated:
  epel-release.noarch 0:7-14                              ius-release.noarch 0:2-1.el7.ius

Complete!

### 4.1.2 Installation de python-pip:
#### requete
yum install python-pip
#### resultat
[maria_dev@sandbox-hdp ~]$ sudo yum install python-pip
Loaded plugins: fastestmirror, ovl
http://public-repo-1.hortonworks.com/HDP/centos7/2.x/updates/2.6.5.0/repodata/repomd.xml: [Errno 14] HTTP Error 403 - Forbidden
Trying other mirror.
To address this issue please refer to the below wiki article

https://wiki.centos.org/yum-errors

If above article doesn't help to resolve this issue please use https://bugs.centos.org/.

HDP-SOLR-2.6-100                                                                                 | 2.9 kB  00:00:00
http://public-repo-1.hortonworks.com/HDP-UTILS-1.1.0.22/repos/centos7/repodata/repomd.xml: [Errno 14] HTTP Error 403 - Forbidden
Trying other mirror.
http://public-repo-1.hortonworks.com/ambari/centos7/2.x/updates/2.6.2.0/repodata/repomd.xml: [Errno 14] HTTP Error 403 - Forbidden
Trying other mirror.
base                                                                                             | 3.6 kB  00:00:00
epel/x86_64/metalink                                                                             |  24 kB  00:00:00
epel                                                                                             | 4.7 kB  00:00:00
extras                                                                                           | 2.9 kB  00:00:00
ius                                                                                              | 1.3 kB  00:00:00
mysql57-community                                                                                | 2.6 kB  00:00:00
updates                                                                                          | 2.9 kB  00:00:00
(1/10): HDP-SOLR-2.6-100/primary_db                                                              | 2.0 kB  00:00:00
(2/10): base/7/x86_64/group_gz                                                                   | 153 kB  00:00:00
(3/10): epel/x86_64/group_gz                                                                     | 100 kB  00:00:00
(4/10): extras/7/x86_64/primary_db                                                               | 254 kB  00:00:00
(5/10): epel/x86_64/updateinfo                                                                   | 1.0 MB  00:00:00
(6/10): ius/x86_64/primary                                                                       |  40 kB  00:00:00
(7/10): mysql57-community/x86_64/primary_db                                                      | 361 kB  00:00:00
(8/10): epel/x86_64/primary_db                                                                   | 7.0 MB  00:00:03
(9/10): base/7/x86_64/primary_db                                                                 | 6.1 MB  00:00:03
(10/10): updates/7/x86_64/primary_db                                                             |  26 MB  00:00:08
Loading mirror speeds from cached hostfile
 * base: mirror.in2p3.fr
 * epel: mirror.in2p3.fr
 * extras: mirror.in2p3.fr
 * updates: mirror.in2p3.fr
ius                                                                                                             159/159
Resolving Dependencies
--> Running transaction check
---> Package python2-pip.noarch 0:8.1.2-14.el7 will be installed
--> Processing Dependency: python-setuptools for package: python2-pip-8.1.2-14.el7.noarch
--> Running transaction check
---> Package python-setuptools.noarch 0:0.9.8-7.el7 will be installed
--> Processing Dependency: python-backports-ssl_match_hostname for package: python-setuptools-0.9.8-7.el7.noarch
--> Running transaction check
---> Package python-backports-ssl_match_hostname.noarch 0:3.5.0.1-1.el7 will be installed
--> Processing Dependency: python-ipaddress for package: python-backports-ssl_match_hostname-3.5.0.1-1.el7.noarch
--> Processing Dependency: python-backports for package: python-backports-ssl_match_hostname-3.5.0.1-1.el7.noarch
--> Running transaction check
---> Package python-backports.x86_64 0:1.0-8.el7 will be installed
---> Package python-ipaddress.noarch 0:1.0.16-2.el7 will be installed
--> Finished Dependency Resolution

Dependencies Resolved

========================================================================================================================
 Package                                         Arch               Version                      Repository        Size
========================================================================================================================
Installing:
 python2-pip                                     noarch             8.1.2-14.el7                 epel             1.7 M
Installing for dependencies:
 python-backports                                x86_64             1.0-8.el7                    base             5.8 k
 python-backports-ssl_match_hostname             noarch             3.5.0.1-1.el7                base              13 k
 python-ipaddress                                noarch             1.0.16-2.el7                 base              34 k
 python-setuptools                               noarch             0.9.8-7.el7                  base             397 k

Transaction Summary
========================================================================================================================
Install  1 Package (+4 Dependent packages)

Total download size: 2.1 M
Installed size: 9.4 M
Is this ok [y/d/N]: y
Downloading packages:
(1/5): python-backports-1.0-8.el7.x86_64.rpm                                                     | 5.8 kB  00:00:00
(2/5): python-backports-ssl_match_hostname-3.5.0.1-1.el7.noarch.rpm                              |  13 kB  00:00:00
(3/5): python-ipaddress-1.0.16-2.el7.noarch.rpm                                                  |  34 kB  00:00:00
(4/5): python-setuptools-0.9.8-7.el7.noarch.rpm                                                  | 397 kB  00:00:00
(5/5): python2-pip-8.1.2-14.el7.noarch.rpm                                                       | 1.7 MB  00:00:00
------------------------------------------------------------------------------------------------------------------------
Total                                                                                   2.7 MB/s | 2.1 MB  00:00:00
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  Installing : python-backports-1.0-8.el7.x86_64                                                                    1/5
  Installing : python-ipaddress-1.0.16-2.el7.noarch                                                                 2/5
  Installing : python-backports-ssl_match_hostname-3.5.0.1-1.el7.noarch                                             3/5
  Installing : python-setuptools-0.9.8-7.el7.noarch                                                                 4/5
  Installing : python2-pip-8.1.2-14.el7.noarch                                                                      5/5
  Verifying  : python-ipaddress-1.0.16-2.el7.noarch                                                                 1/5
  Verifying  : python2-pip-8.1.2-14.el7.noarch                                                                      2/5
  Verifying  : python-setuptools-0.9.8-7.el7.noarch                                                                 3/5
  Verifying  : python-backports-ssl_match_hostname-3.5.0.1-1.el7.noarch                                             4/5
  Verifying  : python-backports-1.0-8.el7.x86_64                                                                    5/5

Installed:
  python2-pip.noarch 0:8.1.2-14.el7

Dependency Installed:
  python-backports.x86_64 0:1.0-8.el7              python-backports-ssl_match_hostname.noarch 0:3.5.0.1-1.el7
  python-ipaddress.noarch 0:1.0.16-2.el7           python-setuptools.noarch 0:0.9.8-7.el7

Complete!

### 4.1.3. Instalation de de MrJob
pip install pathlib
pip install mrjob==0.7.4
pip install PyYAML==5.4.1
#### installation 1 :
[maria_dev@sandbox-hdp ~]$ sudo pip install pathlib
Collecting pathlib
  Downloading https://files.pythonhosted.org/packages/ac/aa/9b065a76b9af472437a0059f77e8f962fe350438b927cb80184c32f075eb/pathlib-1.0.1.tar.gz (49kB)
    100% |████████████████████████████████| 51kB 1.4MB/s
Installing collected packages: pathlib
  Running setup.py install for pathlib ... done
Successfully installed pathlib-1.0.1
You are using pip version 8.1.2, however version 24.0 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
#### installation 2 :
[maria_dev@sandbox-hdp ~]$ sudo pip install mrjob==0.7.4
Collecting mrjob==0.7.4
  Downloading https://files.pythonhosted.org/packages/8e/58/fc28ab743aba16e90736ad4e29694bd2adaf7b879376ff149306d50c4e90/mrjob-0.7.4-py2.py3-none-any.whl (439kB)
    100% |████████████████████████████████| 440kB 3.6MB/s
Collecting PyYAML>=3.10 (from mrjob==0.7.4)
  Downloading https://files.pythonhosted.org/packages/cd/e5/af35f7ea75cf72f2cd079c95ee16797de7cd71f29ea7c68ae5ce7be1eda0/PyYAML-6.0.1.tar.gz (125kB)
    100% |████████████████████████████████| 133kB 3.5MB/s
Installing collected packages: PyYAML, mrjob
  Running setup.py install for PyYAML ... done
Successfully installed PyYAML-6.0.1 mrjob-0.7.4
You are using pip version 8.1.2, however version 24.0 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
#### installation 3 : 
[maria_dev@sandbox-hdp ~]$ sudo pip install PyYAML==5.4.1
Collecting PyYAML==5.4.1
  Downloading https://files.pythonhosted.org/packages/ba/d4/3cf562876e0cda0405e65d351b835077ab13990e5b92912ef2bf1a2280e0/PyYAML-5.4.1-cp27-cp27mu-manylinux1_x86_64.whl (574kB)
    100% |████████████████████████████████| 583kB 2.2MB/s
Installing collected packages: PyYAML
  Found existing installation: PyYAML 6.0.1
    Uninstalling PyYAML-6.0.1:
      Successfully uninstalled PyYAML-6.0.1
Successfully installed PyYAML-5.4.1
You are using pip version 8.1.2, however version 24.0 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.

### 4.1.4. Instalation de NANO
yum install nano
#### resultat :
[maria_dev@sandbox-hdp ~]$ sudo yum install nano
Loaded plugins: fastestmirror, ovl
http://public-repo-1.hortonworks.com/HDP/centos7/2.x/updates/2.6.5.0/repodata/repomd.xml: [Errno 14] HTTP Error 403 - Forbidden
Trying other mirror.
To address this issue please refer to the below wiki article

https://wiki.centos.org/yum-errors

If above article doesn't help to resolve this issue please use https://bugs.centos.org/.

http://public-repo-1.hortonworks.com/HDP-UTILS-1.1.0.22/repos/centos7/repodata/repomd.xml: [Errno 14] HTTP Error 403 - Forbidden
Trying other mirror.
http://public-repo-1.hortonworks.com/ambari/centos7/2.x/updates/2.6.2.0/repodata/repomd.xml: [Errno 14] HTTP Error 403 - Forbidden
Trying other mirror.
Loading mirror speeds from cached hostfile
 * base: fr2.rpmfind.net
 * epel: fr2.rpmfind.net
 * extras: fr2.rpmfind.net
 * updates: fr2.rpmfind.net
Resolving Dependencies
--> Running transaction check
---> Package nano.x86_64 0:2.3.1-10.el7 will be installed
--> Finished Dependency Resolution

Dependencies Resolved

========================================================================================================================
 Package                  Arch                       Version                             Repository                Size
========================================================================================================================
Installing:
 nano                     x86_64                     2.3.1-10.el7                        base                     440 k

Transaction Summary
========================================================================================================================
Install  1 Package

Total download size: 440 k
Installed size: 1.6 M
Is this ok [y/d/N]: y
Downloading packages:
nano-2.3.1-10.el7.x86_64.rpm                                                                     | 440 kB  00:00:00
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  Installing : nano-2.3.1-10.el7.x86_64                                                                             1/1
  Verifying  : nano-2.3.1-10.el7.x86_64                                                                             1/1

Installed:
  nano.x86_64 0:2.3.1-10.el7

Complete!


## 4.2 Execution du MapReduce en local
rebasculer sur l'utilisateur maria_dev
### requete
su

### 4.2.1. Récuperation du code et des données
#### question 1 : commenter la commande dessous
wget https://github.com/juba-agoun/iut-hadoop/raw/main/filmEvaluation.py
charge dans la vm le fichier du lien spécifié
##### resultat :
[maria_dev@sandbox-hdp ~]$ wget https://github.com/juba-agoun/iut-hadoop/raw/main/filmEvaluation.py
--2024-03-28 09:50:11--  https://github.com/juba-agoun/iut-hadoop/raw/main/filmEvaluation.py
Resolving github.com (github.com)... 140.82.121.4
Connecting to github.com (github.com)|140.82.121.4|:443... connected.
HTTP request sent, awaiting response... 302 Found
Location: https://raw.githubusercontent.com/juba-agoun/iut-hadoop/main/filmEvaluation.py [following]
--2024-03-28 09:50:11--  https://raw.githubusercontent.com/juba-agoun/iut-hadoop/main/filmEvaluation.py
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.108.133, 185.199.109.133, 185.199.111.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.108.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 513 [text/plain]
Saving to: ‘filmEvaluation.py’

100%[==============================================================================>] 513         --.-K/s   in 0s

2024-03-28 09:50:11 (48.2 MB/s) - ‘filmEvaluation.py’ saved [513/513]

#### question 2 : commenter la commande dessous
wget https://github.com/juba-agoun/iut-hadoop/raw/main/evaluation.data
##### resultat :
wget https://github.com/juba-agoun/iut-hadoop/raw/main/evaluation.data
--2024-03-28 09:51:37--  https://github.com/juba-agoun/iut-hadoop/raw/main/evaluation.data
Resolving github.com (github.com)... 140.82.121.4
Connecting to github.com (github.com)|140.82.121.4|:443... connected.
HTTP request sent, awaiting response... 302 Found
Location: https://raw.githubusercontent.com/juba-agoun/iut-hadoop/main/evaluation.data [following]
--2024-03-28 09:51:37--  https://raw.githubusercontent.com/juba-agoun/iut-hadoop/main/evaluation.data
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.108.133, 185.199.109.133, 185.199.111.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.108.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1979226 (1.9M) [text/plain]
Saving to: ‘evaluation.data’

100%[==============================================================================>] 1,979,226   9.33MB/s   in 0.2s

2024-03-28 09:51:37 (9.33 MB/s) - ‘evaluation.data’ saved [1979226/1979226]

#### si erreur, changer la configuration de la vm pour les 
#### les 2 commandes suivantes servent à charger importater fichier spécifié dans le lien dans la vm
#### pour wget on peu aussi utiliser "wget --no-check-certificate"
### vérification du programme map reduce
[maria_dev@sandbox-hdp ~]$ python filmEvaluation.py evaluation.data
No configs found; falling back on auto-configuration
No configs specified for inline runner
Creating temp directory /tmp/filmEvaluation.maria_dev.20240328.103041.438782
Running step 1 of 1...
job output is in /tmp/filmEvaluation.maria_dev.20240328.103041.438782/output
Streaming final output from /tmp/filmEvaluation.maria_dev.20240328.103041.438782/output...
"4"     34174
"5"     21203
"1"     6111
"2"     11370
"3"     27145
Removing temp directory /tmp/filmEvaluation.maria_dev.20240328.103041.438782...


## 4.3. Execution du MapReduce sur Hadoop
commente moi ce résultat
[maria_dev@sandbox-hdp ~]$ python filmEvaluation.py -r hadoop --hadoop-streaming-jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar hdfs:///user/maria_dev/new_data/evaluation.data
No configs found; falling back on auto-configuration
No configs specified for hadoop runner
Looking for hadoop binary in $PATH...
Found hadoop binary: /usr/bin/hadoop
Using Hadoop version 2.7.3.2.6.5.0
Creating temp directory /tmp/filmEvaluation.maria_dev.20240328.103810.048495
uploading working dir files to hdfs:///user/maria_dev/tmp/mrjob/filmEvaluation.maria_dev.20240328.103810.048495/files/wd...
Copying other local files to hdfs:///user/maria_dev/tmp/mrjob/filmEvaluation.maria_dev.20240328.103810.048495/files/
Running step 1 of 1...
  packageJobJar: [] [/usr/hdp/2.6.5.0-292/hadoop-mapreduce/hadoop-streaming-2.7.3.2.6.5.0-292.jar] /tmp/streamjob1720527899811415826.jar tmpDir=null
  Connecting to ResourceManager at sandbox-hdp.hortonworks.com/172.18.0.2:8032
  Connecting to Application History server at sandbox-hdp.hortonworks.com/172.18.0.2:10200
  Connecting to ResourceManager at sandbox-hdp.hortonworks.com/172.18.0.2:8032
  Connecting to Application History server at sandbox-hdp.hortonworks.com/172.18.0.2:10200
  Total input paths to process : 1
  number of splits:2
  Submitting tokens for job: job_1711619765382_0001
  Submitted application application_1711619765382_0001
  The url to track the job: http://sandbox-hdp.hortonworks.com:8088/proxy/application_1711619765382_0001/
  Running job: job_1711619765382_0001
  Job job_1711619765382_0001 running in uber mode : false
   map 0% reduce 0%
   map 50% reduce 0%
   map 100% reduce 0%
   map 100% reduce 100%
  Job job_1711619765382_0001 completed successfully
  Application state is completed. FinalApplicationStatus=SUCCEEDED. Redirecting to job history server
  Output directory: hdfs:///user/maria_dev/tmp/mrjob/filmEvaluation.maria_dev.20240328.103810.048495/output
Counters: 49
        File Input Format Counters
                Bytes Read=2038189
        File Output Format Counters
                Bytes Written=49
        File System Counters
                FILE: Number of bytes read=800030
                FILE: Number of bytes written=2072784
                FILE: Number of large read operations=0
                FILE: Number of read operations=0
                FILE: Number of write operations=0
                HDFS: Number of bytes read=2038451
                HDFS: Number of bytes written=49
                HDFS: Number of large read operations=0
                HDFS: Number of read operations=9
                HDFS: Number of write operations=2
        Job Counters
                Data-local map tasks=2
                Launched map tasks=2
                Launched reduce tasks=1
                Total megabyte-milliseconds taken by all map tasks=7153500
                Total megabyte-milliseconds taken by all reduce tasks=3537250
                Total time spent by all map tasks (ms)=28614
                Total time spent by all maps in occupied slots (ms)=28614
                Total time spent by all reduce tasks (ms)=14149
                Total time spent by all reduces in occupied slots (ms)=14149
                Total vcore-milliseconds taken by all map tasks=28614
                Total vcore-milliseconds taken by all reduce tasks=14149
        Map-Reduce Framework
                CPU time spent (ms)=39710
                Combine input records=0
                Combine output records=0
                Failed Shuffles=0
                GC time elapsed (ms)=6859
                Input split bytes=262
                Map input records=100003
                Map output bytes=600018
                Map output materialized bytes=800036
                Map output records=100003
                Merged Map outputs=2
                Physical memory (bytes) snapshot=551030784
                Reduce input groups=5
                Reduce input records=100003
                Reduce output records=5
                Reduce shuffle bytes=800036
                Shuffled Maps =2
                Spilled Records=200006
                Total committed heap usage (bytes)=276824064
                Virtual memory (bytes) snapshot=5866561536
        Shuffle Errors
                BAD_ID=0
                CONNECTION=0
                IO_ERROR=0
                WRONG_LENGTH=0
                WRONG_MAP=0
                WRONG_REDUCE=0
job output is in hdfs:///user/maria_dev/tmp/mrjob/filmEvaluation.maria_dev.20240328.103810.048495/output
Streaming final output from hdfs:///user/maria_dev/tmp/mrjob/filmEvaluation.maria_dev.20240328.103810.048495/output...
"1"     6111
"2"     11370
"3"     27145
"4"     34174
"5"     21203
Removing HDFS temp directory hdfs:///user/maria_dev/tmp/mrjob/filmEvaluation.maria_dev.20240328.103810.048495...
Removing temp directory /tmp/filmEvaluation.maria_dev.20240328.103810.048495...
### explication :
le job MapReduce a réussi à traiter le fichier d'entrée evaluation.data et a produit les résultats souhaités, qui sont le nombre d'évaluations pour chaque film.
Par exemple, le film avec l'identifiant "1" a reçu 6111 évaluations.

# 5.Mise en pratique Exam
## Avec la fconfiguration par défaut de hadoop
### question 1 : Trouvez combien de tags chaque film possède?
utiliser vi pour crer et modifier le fichier 
faire tourner le code avec la requete suivante
python count_film.py -r hadoop --hadoop-streaming-jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar hdfs:///user/maria_dev/new_data/tags.csv -o hdfs///results/tags_output_nouveau
afficher le fichier
hdfs fs -cat hdfs:///user/maria_dev/hdfs///results/tags_output_nouveau/part-00000
### question 2 : Trouvez combien de tags chaque utilisateur a ajoutés? :
utiliser vi pour crer et modifier le fichier 
faire tourner le code avec la requete suivante
python count_user.py -r hadoop --hadoop-streaming-jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar hdfs:///user/maria_dev/new_data/tags.csv -o hdfs///results/tags_output_nouveau_bis
afficher le fichier
hdfs fs -cat hdfs:///user/maria_dev/hdfs///results/tags_output_nouveau_bis/part-00000
## Avec la configuration de Hadoop suivante (taille du bloc = par défaut et taille du bloc = 64 Mo)
### question 3 : Combien de blocs occupe le fichier dans HDFS dans chacune des configurations ?
#### avec la configuration de base 128
hdfs fsck /user/maria_dev/new_data/tags.csv -files -blocks
##### resultat:
```sh
[maria_dev@sandbox-hdp ~]$ hdfs fsck /user/maria_dev/new_data/tags.csv -files -blocks
Connecting to namenode via http://sandbox-hdp.hortonworks.com:50070/fsck?ugi=maria_dev&files=1&blocks=1&path=%2Fuser%2Fmaria_dev%2Fnew_data%2Ftags.csv
FSCK started by maria_dev (auth:SIMPLE) from /172.18.0.2 for path /user/maria_dev/new_data/tags.csv at Thu Mar 28 12:40:43 UTC 2024
/user/maria_dev/new_data/tags.csv 38810332 bytes, 1 block(s):  OK
0. BP-243674277-172.17.0.2-1529333510191:blk_1073743086_2270 len=38810332 repl=1

Status: HEALTHY
 Total size:    38810332 B
 Total dirs:    0
 Total files:   1
 Total symlinks:                0
 Total blocks (validated):      1 (avg. block size 38810332 B)
 Minimally replicated blocks:   1 (100.0 %)
 Over-replicated blocks:        0 (0.0 %)
 Under-replicated blocks:       0 (0.0 %)
 Mis-replicated blocks:         0 (0.0 %)
 Default replication factor:    1
 Average block replication:     1.0
 Corrupt blocks:                0
 Missing replicas:              0 (0.0 %)
 Number of data-nodes:          1
 Number of racks:               1
FSCK ended at Thu Mar 28 12:40:43 UTC 2024 in 15 milliseconds


The filesystem under path '/user/maria_dev/new_data/tags.csv' is HEALTHY
```
##### explication :
seulement sur 1 block 

#### avec la configuration 64
hdfs dfs -D dfs.blocksize=67108864 -put /user/maria_dev/new_data/tags.csv
```sh
[maria_dev@sandbox-hdp ~]$ hdfs fsck /user/maria_dev/new_data/tags.csv -files -blocks
Connecting to namenode via http://sandbox-hdp.hortonworks.com:50070/fsck?ugi=maria_dev&files=1&blocks=1&path=%2Fuser%2Fmaria_dev%2Fnew_data%2Ftags.csv
FSCK started by maria_dev (auth:SIMPLE) from /172.18.0.2 for path /user/maria_dev/new_data/tags.csv at Thu Mar 28 12:40:43 UTC 2024
/user/maria_dev/new_data/tags.csv 38810332 bytes, 1 block(s):  OK
0. BP-243674277-172.17.0.2-1529333510191:blk_1073743086_2270 len=38810332 repl=1

Status: HEALTHY
 Total size:    38810332 B
 Total dirs:    0
 Total files:   1
 Total symlinks:                0
 Total blocks (validated):      1 (avg. block size 38810332 B)
 Minimally replicated blocks:   1 (100.0 %)
 Over-replicated blocks:        0 (0.0 %)
 Under-replicated blocks:       0 (0.0 %)
 Mis-replicated blocks:         0 (0.0 %)
 Default replication factor:    1
 Average block replication:     1.0
 Corrupt blocks:                0
 Missing replicas:              0 (0.0 %)
 Number of data-nodes:          1
 Number of racks:               1
FSCK ended at Thu Mar 28 12:40:43 UTC 2024 in 15 milliseconds


The filesystem under path '/user/maria_dev/new_data/tags.csv' is HEALTHY
```

##### explication :
seulement sur 1 block 


### repasser en configuration de base 
hdfs dfsadmin -setBlockSize 134217728 /

### question 4 :
utiliser vi pour crer et modifier le fichier 
faire tourner le code avec la requete suivante
python count_tags_tags.py -r hadoop --hadoop-streaming-jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar hdfs:///user/maria_dev/new_data/tags.csv -o hdfs///results/tags_output_nouveau_bis_bis
afficher le fichier
hdfs fs -cat hdfs:///user/maria_dev/hdfs///results/tags_output_nouveau_bis_bis/part-00000