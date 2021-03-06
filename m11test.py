{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Intellisense\n",
    "\n",
    "%config IPCompleter.greedy=True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {},
   "outputs": [],
   "source": [
    "PROJECT_ID = 'test-big-ms-277323'\n",
    "\n",
    "#create a client instance for you project\n",
    "from google.cloud import bigquery\n",
    "from google.oauth2 import service_account\n",
    "creds = service_account.Credentials.from_service_account_file(r\"C:\\Users\\varunn\\Documents\\kaggle-competiton\\credentials\\test-big-ms-277323.json\")\n",
    "client = bigquery.Client(project=PROJECT_ID,location='US',credentials=creds)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Dataset(DatasetReference('test-big-ms-277323', 'new_dataset'))"
      ]
     },
     "execution_count": 85,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#create a new dataset\n",
    "client.create_dataset('new_dataset')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Table(TableReference(DatasetReference('test-big-ms-277323', 'new_dataset'), 'new_table'))"
      ]
     },
     "execution_count": 86,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#create a table in dataset\n",
    "client.create_table(f\"{PROJECT_ID}.new_dataset.new_table\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "fd = (r\"C:\\Users\\varunn\\Documents\\Confluence attachments\\MarketingSci Regression analysis\\adspendraw\\merged_df.xlsx\")\n",
    "adspend = pd.read_excel(fd,sheet_name=0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [],
   "source": [
    "adspend.columns = adspend.iloc[0,:]\n",
    "adspend = adspend.drop(0)\n",
    "adspend = adspend.fillna(0)\n",
    "adspend = adspend.rename(columns = {adspend.columns[0]:'first'})\n",
    "adspend = adspend.drop('first', axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [],
   "source": [
    "adspend = adspend.iloc[:,0:11]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['MEDIA', 'INDUSTRY', 'Jan2000', 'Feb2000', 'mar2000', 'apr2000',\n",
       "       'may2000', 'jun2000', 'jul2000', 'aug2000', 'sep2000'],\n",
       "      dtype='object', name=0)"
      ]
     },
     "execution_count": 75,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "adspend.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "adspend = adspend.rename(columns={'JAN 2000  DOLS (000)':'Jan2000','FEB 2000  DOLS (000)':'Feb2000','MAR 2000  DOLS (000)':'mar2000', 'APR 2000  DOLS (000)':'apr2000', 'MAY 2000  DOLS (000)':'may2000',\n",
    "       'JUN 2000  DOLS (000)':'jun2000', 'JUL 2000  DOLS (000)':'jul2000', 'AUG 2000  DOLS (000)':'aug2000',\n",
    "       'SEP 2000  DOLS (000)':'sep2000'})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "loaded 1123 rows into new_dataset:new_table\n"
     ]
    }
   ],
   "source": [
    "dataset_id = 'new_dataset'\n",
    "table_id = 'new_table'\n",
    "\n",
    "#tell client everything it needs to know to upload your data\n",
    "dataset_ref = client.dataset(dataset_id)\n",
    "table_ref = dataset_ref.table(table_id)\n",
    "job_config = bigquery.LoadJobConfig(schema=[\n",
    "        # Specify the type of columns whose type cannot be auto-detected. For\n",
    "        # example the \"title\" column uses pandas dtype \"object\", so its\n",
    "        # data type is ambiguous.\n",
    "        bigquery.SchemaField(\"MEDIA\", bigquery.enums.SqlTypeNames.STRING),\n",
    "        # Indexes are written if included in the schema by name.\n",
    "        bigquery.SchemaField(\"INDUSTRY\", bigquery.enums.SqlTypeNames.STRING),\n",
    "    ],)\n",
    "job_config.autodetect = True\n",
    "\n",
    "job = client.load_table_from_dataframe(adspend,table_ref,job_config=job_config)\n",
    "job.result()\n",
    "print (\"loaded {} rows into {}:{}\".format(job.output_rows,dataset_id,table_id))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>MEDIA</th>\n",
       "      <th>INDUSTRY</th>\n",
       "      <th>Jan2000</th>\n",
       "      <th>Feb2000</th>\n",
       "      <th>mar2000</th>\n",
       "      <th>apr2000</th>\n",
       "      <th>may2000</th>\n",
       "      <th>jun2000</th>\n",
       "      <th>jul2000</th>\n",
       "      <th>aug2000</th>\n",
       "      <th>sep2000</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Network TV</td>\n",
       "      <td>Ready-To-Wear, Formalwear &amp; Bridalwear</td>\n",
       "      <td>509.7</td>\n",
       "      <td>457.0</td>\n",
       "      <td>4557.1</td>\n",
       "      <td>5161.6</td>\n",
       "      <td>5546.5</td>\n",
       "      <td>1752.0</td>\n",
       "      <td>699.5</td>\n",
       "      <td>5092.2</td>\n",
       "      <td>11982.5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Network TV</td>\n",
       "      <td>Underclothing &amp; Hosiery</td>\n",
       "      <td>0.0</td>\n",
       "      <td>388.8</td>\n",
       "      <td>2101.3</td>\n",
       "      <td>1321.7</td>\n",
       "      <td>1293.2</td>\n",
       "      <td>113.4</td>\n",
       "      <td>880.2</td>\n",
       "      <td>1422.8</td>\n",
       "      <td>1564.3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Network TV</td>\n",
       "      <td>Footwear</td>\n",
       "      <td>18219.2</td>\n",
       "      <td>10392.3</td>\n",
       "      <td>15939.7</td>\n",
       "      <td>19169.9</td>\n",
       "      <td>21465.5</td>\n",
       "      <td>26096.6</td>\n",
       "      <td>11941.1</td>\n",
       "      <td>16772.5</td>\n",
       "      <td>21668.1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Network TV</td>\n",
       "      <td>Jewelry &amp; Watches</td>\n",
       "      <td>197.7</td>\n",
       "      <td>2391.6</td>\n",
       "      <td>1490.8</td>\n",
       "      <td>3553.8</td>\n",
       "      <td>1675.2</td>\n",
       "      <td>1978.7</td>\n",
       "      <td>1587.9</td>\n",
       "      <td>1549.4</td>\n",
       "      <td>1746.3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Network TV</td>\n",
       "      <td>Apparel NEC</td>\n",
       "      <td>1650.9</td>\n",
       "      <td>2534.1</td>\n",
       "      <td>588.3</td>\n",
       "      <td>484.0</td>\n",
       "      <td>5926.7</td>\n",
       "      <td>1564.6</td>\n",
       "      <td>647.1</td>\n",
       "      <td>634.0</td>\n",
       "      <td>884.6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Network TV</td>\n",
       "      <td>Financial</td>\n",
       "      <td>184593.9</td>\n",
       "      <td>74905.1</td>\n",
       "      <td>140728.2</td>\n",
       "      <td>98110.6</td>\n",
       "      <td>92704.0</td>\n",
       "      <td>71286.0</td>\n",
       "      <td>48302.9</td>\n",
       "      <td>42076.2</td>\n",
       "      <td>171124.6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Network TV</td>\n",
       "      <td>Communications</td>\n",
       "      <td>138277.8</td>\n",
       "      <td>81281.6</td>\n",
       "      <td>98965.0</td>\n",
       "      <td>80275.2</td>\n",
       "      <td>108233.8</td>\n",
       "      <td>76408.6</td>\n",
       "      <td>38107.4</td>\n",
       "      <td>67228.9</td>\n",
       "      <td>153281.6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Network TV</td>\n",
       "      <td>Government, Politics &amp; Organizations</td>\n",
       "      <td>92640.2</td>\n",
       "      <td>96953.1</td>\n",
       "      <td>130341.2</td>\n",
       "      <td>119356.2</td>\n",
       "      <td>133782.2</td>\n",
       "      <td>91898.0</td>\n",
       "      <td>72064.7</td>\n",
       "      <td>75212.8</td>\n",
       "      <td>92669.8</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Network TV</td>\n",
       "      <td>Insurance &amp; Real Estate</td>\n",
       "      <td>27171.2</td>\n",
       "      <td>22573.3</td>\n",
       "      <td>41010.7</td>\n",
       "      <td>46502.4</td>\n",
       "      <td>37074.4</td>\n",
       "      <td>29092.0</td>\n",
       "      <td>18045.8</td>\n",
       "      <td>19960.5</td>\n",
       "      <td>42535.5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>Network TV</td>\n",
       "      <td>Computers, Software, Internet NEC</td>\n",
       "      <td>85004.9</td>\n",
       "      <td>30172.0</td>\n",
       "      <td>71531.6</td>\n",
       "      <td>55155.6</td>\n",
       "      <td>73659.1</td>\n",
       "      <td>61965.9</td>\n",
       "      <td>30129.4</td>\n",
       "      <td>35001.9</td>\n",
       "      <td>84284.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        MEDIA                                INDUSTRY   Jan2000  Feb2000  \\\n",
       "0  Network TV  Ready-To-Wear, Formalwear & Bridalwear     509.7    457.0   \n",
       "1  Network TV                 Underclothing & Hosiery       0.0    388.8   \n",
       "2  Network TV                                Footwear   18219.2  10392.3   \n",
       "3  Network TV                       Jewelry & Watches     197.7   2391.6   \n",
       "4  Network TV                             Apparel NEC    1650.9   2534.1   \n",
       "5  Network TV                               Financial  184593.9  74905.1   \n",
       "6  Network TV                          Communications  138277.8  81281.6   \n",
       "7  Network TV    Government, Politics & Organizations   92640.2  96953.1   \n",
       "8  Network TV                 Insurance & Real Estate   27171.2  22573.3   \n",
       "9  Network TV       Computers, Software, Internet NEC   85004.9  30172.0   \n",
       "\n",
       "    mar2000   apr2000   may2000  jun2000  jul2000  aug2000   sep2000  \n",
       "0    4557.1    5161.6    5546.5   1752.0    699.5   5092.2   11982.5  \n",
       "1    2101.3    1321.7    1293.2    113.4    880.2   1422.8    1564.3  \n",
       "2   15939.7   19169.9   21465.5  26096.6  11941.1  16772.5   21668.1  \n",
       "3    1490.8    3553.8    1675.2   1978.7   1587.9   1549.4    1746.3  \n",
       "4     588.3     484.0    5926.7   1564.6    647.1    634.0     884.6  \n",
       "5  140728.2   98110.6   92704.0  71286.0  48302.9  42076.2  171124.6  \n",
       "6   98965.0   80275.2  108233.8  76408.6  38107.4  67228.9  153281.6  \n",
       "7  130341.2  119356.2  133782.2  91898.0  72064.7  75212.8   92669.8  \n",
       "8   41010.7   46502.4   37074.4  29092.0  18045.8  19960.5   42535.5  \n",
       "9   71531.6   55155.6   73659.1  61965.9  30129.4  35001.9   84284.0  "
      ]
     },
     "execution_count": 88,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#query the data\n",
    "query = f\"\"\" Select * from {PROJECT_ID}.new_dataset.new_table limit 10\"\"\"\n",
    "query_job = client.query(query)\n",
    "data = query_job.to_dataframe()\n",
    "data.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
