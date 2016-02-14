#!/bin/bash
#change all events to correct value

sed -i -e 's/ Column/ db.Column/g' $1
sed -i -e 's/INTEGER/db.Integer/g' $1
sed -i -e 's/VARCHAR/db.String/g' $1
sed -i -e 's/ relationship/ db.relationship/g' $1