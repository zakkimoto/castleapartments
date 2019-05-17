# Generated by Django 2.2.1 on 2019-05-17 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_auto_20190517_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='country',
            field=models.CharField(choices=[('Andorra', 'Andorra'), ('United Arab Emirates', 'United Arab Emirates'), ('Afghanistan', 'Afghanistan'), ('Antigua & Barbuda', 'Antigua & Barbuda'), ('Anguilla', 'Anguilla'), ('Albania', 'Albania'), ('Armenia', 'Armenia'), ('Netherlands Antilles', 'Netherlands Antilles'), ('Angola', 'Angola'), ('Antarctica', 'Antarctica'), ('Argentina', 'Argentina'), ('American Samoa', 'American Samoa'), ('Austria', 'Austria'), ('Australia', 'Australia'), ('Aruba', 'Aruba'), ('Azerbaijan', 'Azerbaijan'), ('Bosnia and Herzegovina', 'Bosnia and Herzegovina'), ('Barbados', 'Barbados'), ('Bangladesh', 'Bangladesh'), ('Belgium', 'Belgium'), ('Burkina Faso', 'Burkina Faso'), ('Bulgaria', 'Bulgaria'), ('Bahrain', 'Bahrain'), ('Burundi', 'Burundi'), ('Benin', 'Benin'), ('Bermuda', 'Bermuda'), ('Brunei Darussalam', 'Brunei Darussalam'), ('Bolivia', 'Bolivia'), ('Brazil', 'Brazil'), ('Bahama', 'Bahama'), ('Bhutan', 'Bhutan'), ('Bouvet Island', 'Bouvet Island'), ('Botswana', 'Botswana'), ('Belarus', 'Belarus'), ('Belize', 'Belize'), ('Canada', 'Canada'), ('Cocos (Keeling) Islands', 'Cocos (Keeling) Islands'), ('Central African Republic', 'Central African Republic'), ('Congo', 'Congo'), ('Switzerland', 'Switzerland'), ('Ivory Coast', 'Ivory Coast'), ('Cook Iisland', 'Cook Iislands'), ('Chile', 'Chile'), ('Cameroon', 'Cameroon'), ('China', 'China'), ('Colombia', 'Colombia'), ('Costa Rica', 'Costa Rica'), ('Cuba', 'Cuba'), ('Cape Verde', 'Cape Verde'), ('Christmas Island', 'Christmas Island'), ('Cyprus', 'Cyprus'), ('Czech Republic', 'Czech Republic'), ('Germany', 'Germany'), ('Djibouti', 'Djibouti'), ('Denmark', 'Denmark'), ('Dominica', 'Dominica'), ('Dominican Republic', 'Dominican Republic'), ('Algeria', 'Algeria'), ('Ecuador', 'Ecuador'), ('Estonia', 'Estonia'), ('Egypt', 'Egypt'), ('Western Sahara', 'Western Sahara'), ('Eritrea', 'Eritrea'), ('Spain', 'Spain'), ('Ethiopia', 'Ethiopia'), ('Finland', 'Finland'), ('Fiji', 'Fiji'), ('Falkland Islands (Malvinas)', 'Falkland Islands (Malvinas)'), ('Micronesia', 'Micronesia'), ('Faroe Islands', 'Faroe Islands'), ('France', 'France'), ('France, Metropolitan', 'France, Metropolitan'), ('Gabon', 'Gabon'), ('United Kingdom (Great Britain)', 'United Kingdom (Great Britain)'), ('Grenada', 'Grenada'), ('Georgia', 'Georgia'), ('French Guiana', 'French Guiana'), ('Ghana', 'Ghana'), ('Gibraltar', 'Gibraltar'), ('Greenland', 'Greenland'), ('Gambia', 'Gambia'), ('Guinea', 'Guinea'), ('Guadeloupe', 'Guadeloupe'), ('Equatorial Guinea', 'Equatorial Guinea'), ('Greece', 'Greece'), ('South Georgia and the South Sandwich Islands', 'South Georgia and the South Sandwich Islands'), ('Guatemala', 'Guatemala'), ('Guam', 'Guam'), ('Guinea-Bissau', 'Guinea-Bissau'), ('Guyana', 'Guyana'), ('Hong Kong', 'Hong Kong'), ('Heard & McDonald Islands', 'Heard & McDonald Islands'), ('Honduras', 'Honduras'), ('Croatia', 'Croatia'), ('Haiti', 'Haiti'), ('Hungary', 'Hungary'), ('Indonesia', 'Indonesia'), ('Ireland', 'Ireland'), ('Israel', 'Israel'), ('India', 'India'), ('British Indian Ocean Territory', 'British Indian Ocean Territory'), ('Iraq', 'Iraq'), ('Islamic Republic of Iran', 'Islamic Republic of Iran'), ('Iceland', 'Iceland'), ('Italy', 'Italy'), ('Jamaica', 'Jamaica'), ('Jordan', 'Jordan'), ('Japan', 'Japan'), ('Kenya', 'Kenya'), ('Kyrgyzstan', 'Kyrgyzstan'), ('Cambodia', 'Cambodia'), ('Kiribati', 'Kiribati'), ('Comoros', 'Comoros'), ('St. Kitts and Nevis', 'St. Kitts and Nevis'), ("Korea, Democratic People's Republic of", "Korea, Democratic People's Republic of"), ('Korea, Republic of', 'Korea, Republic of'), ('Kuwait', 'Kuwait'), ('Cayman Islands', 'Cayman Islands'), ('Kazakhstan', 'Kazakhstan'), ("Lao People's Democratic Republic", "Lao People's Democratic Republic"), ('Lebanon', 'Lebanon'), ('Saint Lucia', 'Saint Lucia'), ('Liechtenstein', 'Liechtenstein'), ('Sri Lanka', 'Sri Lanka'), ('Liberia', 'Liberia'), ('Lesotho', 'Lesotho'), ('Lithuania', 'Lithuania'), ('Luxembourg', 'Luxembourg'), ('Latvia', 'Latvia'), ('Libyan Arab Jamahiriya', 'Libyan Arab Jamahiriya'), ('Morocco', 'Morocco'), ('Monaco', 'Monaco'), ('Moldova, Republic of', 'Moldova, Republic of'), ('Madagascar', 'Madagascar'), ('Marshall Islands', 'Marshall Islands'), ('Mali', 'Mali'), ('Mongolia', 'Mongolia'), ('Myanmar', 'Myanmar'), ('Macau', 'Macau'), ('Northern Mariana Islands', 'Northern Mariana Islands'), ('Martinique', 'Martinique'), ('Mauritania', 'Mauritania'), ('Monserrat', 'Monserrat'), ('Malta', 'Malta'), ('Mauritius', 'Mauritius'), ('Maldives', 'Maldives'), ('Malawi', 'Malawi'), ('Mexico', 'Mexico'), ('Malaysia', 'Malaysia'), ('Mozambique', 'Mozambique'), ('Namibia', 'Namibia'), ('New Caledonia', 'New Caledonia'), ('Niger', 'Niger'), ('Norfolk Island', 'Norfolk Island'), ('Nigeria', 'Nigeria'), ('Nicaragua', 'Nicaragua'), ('Netherlands', 'Netherlands'), ('Norway', 'Norway'), ('Nepal', 'Nepal'), ('Nauru', 'Nauru'), ('Niue', 'Niue'), ('New Zealand', 'New Zealand'), ('Oman', 'Oman'), ('Panama', 'Panama'), ('Peru', 'Peru'), ('French Polynesia', 'French Polynesia'), ('Papua New Guinea', 'Papua New Guinea'), ('Philippines', 'Philippines'), ('Pakistan', 'Pakistan'), ('Poland', 'Poland'), ('St. Pierre & Miquelon', 'St. Pierre & Miquelon'), ('Pitcairn', 'Pitcairn'), ('Puerto Rico', 'Puerto Rico'), ('Portugal', 'Portugal'), ('Palau', 'Palau'), ('Paraguay', 'Paraguay'), ('Qatar', 'Qatar'), ('Reunion', 'Reunion'), ('Romania', 'Romania'), ('Russian Federation', 'Russian Federation'), ('Rwanda', 'Rwanda'), ('Saudi Arabia', 'Saudi Arabia'), ('Solomon Islands', 'Solomon Islands'), ('Seychelles', 'Seychelles'), ('Sudan', 'Sudan'), ('Sweden', 'Sweden'), ('Singapore', 'Singapore'), ('St. Helena', 'St. Helena'), ('Slovenia', 'Slovenia'), ('Svalbard & Jan Mayen Islands', 'Svalbard & Jan Mayen Islands'), ('Slovakia', 'Slovakia'), ('Sierra Leone', 'Sierra Leone'), ('San Marino', 'San Marino'), ('Senegal', 'Senegal'), ('Somalia', 'Somalia'), ('Suriname', 'Suriname'), ('Sao Tome & Principe', 'Sao Tome & Principe'), ('El Salvador', 'El Salvador'), ('Syrian Arab Republic', 'Syrian Arab Republic'), ('Swaziland', 'Swaziland'), ('Turks & Caicos Islands', 'Turks & Caicos Islands'), ('Chad', 'Chad'), ('French Southern Territories', 'French Southern Territories'), ('Togo', 'Togo'), ('Thailand', 'Thailand'), ('Tajikistan', 'Tajikistan'), ('Tokelau', 'Tokelau'), ('Turkmenistan', 'Turkmenistan'), ('Tunisia', 'Tunisia'), ('Tonga', 'Tonga'), ('East Timor', 'East Timor'), ('Turkey', 'Turkey'), ('Trinidad & Tobago', 'Trinidad & Tobago'), ('Tuvalu', 'Tuvalu'), ('Taiwan, Province of China', 'Taiwan, Province of China'), ('Tanzania, United Republic of', 'Tanzania, United Republic of'), ('Ukraine', 'Ukraine'), ('Uganda', 'Uganda'), ('United States Minor Outlying Islands', 'United States Minor Outlying Islands'), ('United States of America', 'United States of America'), ('Uruguay', 'Uruguay'), ('Uzbekistan', 'Uzbekistan'), ('Vatican City State (Holy See)', 'Vatican City State (Holy See)'), ('St. Vincent & the Grenadines', 'St. Vincent & the Grenadines'), ('Venezuela', 'Venezuela'), ('British Virgin Islands', 'British Virgin Islands'), ('United States Virgin Islands', 'United States Virgin Islands'), ('Viet Nam', 'Viet Nam'), ('Vanuatu', 'Vanuatu'), ('Wallis & Futuna Islands', 'Wallis & Futuna Islands'), ('Samoa', 'Samoa'), ('Yemen', 'Yemen'), ('Mayotte', 'Mayotte'), ('Yugoslavia', 'Yugoslavia'), ('South Africa', 'South Africa'), ('Zambia', 'Zambia'), ('Zaire', 'Zaire'), ('Zimbabwe', 'Zimbabwe'), ('Unknown or unspecified country', 'Unknown or unspecified country')], max_length=100),
        ),
    ]
