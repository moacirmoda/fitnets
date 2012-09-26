svn co https://fw.lab.sp.cefetsp.br/svn/a6pgp/S201202/Fitnets/ svn
cd svn
git clone git://github.com/moacirmoda/fitnets.git git
cp -r git/* .
rm -r git
svn ci -m "Atualizando svn"
cd ..
rm -r svn

