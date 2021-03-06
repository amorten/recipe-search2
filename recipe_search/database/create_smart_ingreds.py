
import MySQLdb
import time


def create_smart_ingreds_1(db,cursor,start_idx):

    
    # Create SmartIngreds1 table
    tablename_ingreds = "SmartIngreds1"
    cursor.execute("""
               CREATE TABLE IF NOT EXISTS"""+' '+tablename_ingreds+' '+"""
               (
                 ingred_id  INT UNSIGNED NOT NULL,
                 PRIMARY KEY (ingred_id),
                 FOREIGN KEY (ingred_id) REFERENCES NaiveIngreds(ingred_id)
                  ON DELETE CASCADE
                  ON UPDATE CASCADE
               ) CHARACTER SET utf8
               """
               )    

    # Get list of NaiveIngredients, in descending order by count
    cursor.execute("""select ing_nums.ingred_id,NaiveIngreds.ingred_text,ing_nums.cnt from (select ingred_id, count(ingred_id) as cnt from recipes_naiveingreds group by ingred_id order by count(ingred_id) desc) as ing_nums JOIN NaiveIngreds on ing_nums.ingred_id=NaiveIngreds.ingred_id order by cnt desc;""")

    all_rows = cursor.fetchall()
    max_idx = len(all_rows)

    idx = start_idx
    while True:

        #Get next unknown naive ingred

        ingred_text = all_rows[idx]['ingred_text']
        ingred_id = all_rows[idx]['ingred_id']
        ingred_cnt = all_rows[idx]['cnt']        
        
        ch = raw_input("Row {}: Is {} (idx={},cnt={}) a good ingredient word (Y=z/N=x/Q)? ".format(idx,ingred_text,ingred_id,ingred_cnt))

        if ch in "YyZz":
            cursor.execute("INSERT IGNORE INTO SmartIngreds1"+
                           "(ingred_id) VALUES "+
                           "(%s)",(ingred_id,))
            db.commit()
            print("Added {} to SmartIngreds1".format(ingred_text))
        elif ch in "NnXx":
            print("Ignored!")
            # Actually, it would be better to check if the ingredient
            # is in SmartIngreds1, in which case it would need to be
            # deleted.
        else:
            return


        idx=idx+1
        
    #cursor.close()

    
    
