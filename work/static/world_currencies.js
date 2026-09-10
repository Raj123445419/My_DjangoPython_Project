/**
 * Universal World Currencies Engine - ALL 195 Countries & Global Currencies
 * Complete 1-to-1 Mapping for Every Country in the World
 * Zero-Error Safe Parsing & Real-Time Conversion Engine
 */

const WORLD_CURRENCY_RATES = {
    // A
    'AFN': { symbol: '؋', rate: 70.50, decimals: 2, label: 'Afghan Afghani', flag: '🇦🇫' },
    'ALL': { symbol: 'L ', rate: 91.20, decimals: 2, label: 'Albanian Lek', flag: '🇦🇱' },
    'DZD': { symbol: 'DA ', rate: 133.50, decimals: 2, label: 'Algerian Dinar', flag: '🇩🇿' },
    'EUR': { symbol: '€', rate: 0.92, decimals: 2, label: 'Euro', flag: '🇪🇺' },
    'AOA': { symbol: 'Kz ', rate: 915.00, decimals: 2, label: 'Angolan Kwanza', flag: '🇦🇴' },
    'XCD': { symbol: 'EC$', rate: 2.70, decimals: 2, label: 'East Caribbean Dollar', flag: '🇦🇬' },
    'ARS': { symbol: 'AR$', rate: 1010.00, decimals: 2, label: 'Argentine Peso', flag: '🇦🇷' },
    'AMD': { symbol: '֏', rate: 388.00, decimals: 2, label: 'Armenian Dram', flag: '🇦🇲' },
    'AUD': { symbol: 'A$', rate: 1.54, decimals: 2, label: 'Australian Dollar', flag: '🇦🇺' },
    'AZN': { symbol: '₼', rate: 1.70, decimals: 2, label: 'Azerbaijani Manat', flag: '🇦🇿' },

    // B
    'BSD': { symbol: 'B$', rate: 1.00, decimals: 2, label: 'Bahamian Dollar', flag: '🇧🇸' },
    'BHD': { symbol: 'BD ', rate: 0.376, decimals: 3, label: 'Bahraini Dinar', flag: '🇧🇭' },
    'BDT': { symbol: '৳', rate: 121.50, decimals: 2, label: 'Bangladeshi Taka', flag: '🇧🇩' },
    'BBD': { symbol: 'Bds$', rate: 2.00, decimals: 2, label: 'Barbadian Dollar', flag: '🇧🇧' },
    'BYN': { symbol: 'Br ', rate: 3.28, decimals: 2, label: 'Belarusian Ruble', flag: '🇧🇾' },
    'BZD': { symbol: 'BZ$', rate: 2.00, decimals: 2, label: 'Belize Dollar', flag: '🇧🇿' },
    'XOF': { symbol: 'CFA ', rate: 605.00, decimals: 0, label: 'West African CFA Franc', flag: '🌍' },
    'BTN': { symbol: 'Nu. ', rate: 87.20, decimals: 2, label: 'Bhutanese Ngultrum', flag: '🇧🇹' },
    'BOB': { symbol: 'Bs ', rate: 6.91, decimals: 2, label: 'Bolivian Boliviano', flag: '🇧🇴' },
    'BAM': { symbol: 'KM ', rate: 1.80, decimals: 2, label: 'Convertible Mark', flag: '🇧🇦' },
    'BWP': { symbol: 'P ', rate: 13.60, decimals: 2, label: 'Botswana Pula', flag: '🇧🇼' },
    'BRL': { symbol: 'R$', rate: 5.65, decimals: 2, label: 'Brazilian Real', flag: '🇧🇷' },
    'BND': { symbol: 'B$', rate: 1.34, decimals: 2, label: 'Brunei Dollar', flag: '🇧🇳' },
    'BGN': { symbol: 'лв ', rate: 1.80, decimals: 2, label: 'Bulgarian Lev', flag: '🇧🇬' },
    'BIF': { symbol: 'FBu ', rate: 2920.00, decimals: 0, label: 'Burundian Franc', flag: '🇧🇮' },

    // C
    'CVE': { symbol: 'Esc ', rate: 101.50, decimals: 2, label: 'Cape Verdean Escudo', flag: '🇨🇻' },
    'KHR': { symbol: '៛ ', rate: 4070.00, decimals: 0, label: 'Cambodian Riel', flag: '🇰🇭' },
    'XAF': { symbol: 'FCFA ', rate: 605.00, decimals: 0, label: 'Central African CFA Franc', flag: '🌍' },
    'CAD': { symbol: 'CA$', rate: 1.38, decimals: 2, label: 'Canadian Dollar', flag: '🇨🇦' },
    'CLP': { symbol: 'CLP$', rate: 960.00, decimals: 0, label: 'Chilean Peso', flag: '🇨🇱' },
    'CNY': { symbol: '¥', rate: 7.24, decimals: 2, label: 'Chinese Yuan', flag: '🇨🇳' },
    'COP': { symbol: 'COL$', rate: 4400.00, decimals: 0, label: 'Colombian Peso', flag: '🇨🇴' },
    'KMF': { symbol: 'CF ', rate: 452.00, decimals: 0, label: 'Comorian Franc', flag: '🇰🇲' },
    'CRC': { symbol: '₡', rate: 512.00, decimals: 2, label: 'Costa Rican Colón', flag: '🇨🇷' },
    'CUP': { symbol: '₱ ', rate: 24.00, decimals: 2, label: 'Cuban Peso', flag: '🇨🇺' },
    'CZK': { symbol: 'Kč ', rate: 23.20, decimals: 2, label: 'Czech Koruna', flag: '🇨🇿' },
    'CDF': { symbol: 'FC ', rate: 2850.00, decimals: 0, label: 'Congolese Franc', flag: '🇨🇩' },

    // D
    'DKK': { symbol: 'kr. ', rate: 6.87, decimals: 2, label: 'Danish Krone', flag: '🇩🇰' },
    'DJF': { symbol: 'Fdj ', rate: 177.72, decimals: 0, label: 'Djiboutian Franc', flag: '🇩🇯' },
    'DOP': { symbol: 'RD$ ', rate: 60.20, decimals: 2, label: 'Dominican Peso', flag: '🇩🇴' },

    // E
    'USD': { symbol: '$', rate: 1.00, decimals: 2, label: 'US Dollar', flag: '🇺🇸' },
    'EGP': { symbol: 'E£ ', rate: 49.30, decimals: 2, label: 'Egyptian Pound', flag: '🇪🇬' },
    'ERN': { symbol: 'Nfk ', rate: 15.00, decimals: 2, label: 'Eritrean Nakfa', flag: '🇪🇷' },
    'SZL': { symbol: 'E ', rate: 18.20, decimals: 2, label: 'Swazi Lilangeni', flag: '🇸🇿' },
    'ETB': { symbol: 'Br ', rate: 122.00, decimals: 2, label: 'Ethiopian Birr', flag: '🇪🇹' },

    // F - G
    'FJD': { symbol: 'FJ$', rate: 2.26, decimals: 2, label: 'Fijian Dollar', flag: '🇫🇯' },
    'GMD': { symbol: 'D ', rate: 71.00, decimals: 2, label: 'Gambian Dalasi', flag: '🇬🇲' },
    'GEL': { symbol: '₾', rate: 2.75, decimals: 2, label: 'Georgian Lari', flag: '🇬🇪' },
    'GHS': { symbol: 'GH₵ ', rate: 16.30, decimals: 2, label: 'Ghanaian Cedi', flag: '🇬🇭' },
    'GTQ': { symbol: 'Q ', rate: 7.73, decimals: 2, label: 'Guatemalan Quetzal', flag: '🇬🇹' },
    'GNF': { symbol: 'FG ', rate: 8600.00, decimals: 0, label: 'Guinean Franc', flag: '🇬🇳' },
    'GYD': { symbol: 'GY$', rate: 209.00, decimals: 2, label: 'Guyanese Dollar', flag: '🇬🇾' },

    // H - I
    'HTG': { symbol: 'G ', rate: 131.50, decimals: 2, label: 'Haitian Gourde', flag: '🇭🇹' },
    'HNL': { symbol: 'L ', rate: 25.10, decimals: 2, label: 'Honduran Lempira', flag: '🇭🇳' },
    'HUF': { symbol: 'Ft ', rate: 365.00, decimals: 0, label: 'Hungarian Forint', flag: '🇭🇺' },
    'ISK': { symbol: 'kr ', rate: 139.00, decimals: 0, label: 'Icelandic Króna', flag: '🇮🇸' },
    'INR': { symbol: '₹', rate: 87.20, decimals: 2, label: 'Indian Rupee', flag: '🇮🇳' },
    'IDR': { symbol: 'Rp ', rate: 16200.00, decimals: 0, label: 'Indonesian Rupiah', flag: '🇮🇩' },
    'IRR': { symbol: '﷼ ', rate: 42000.00, decimals: 0, label: 'Iranian Rial', flag: '🇮🇷' },
    'IQD': { symbol: 'IQD ', rate: 1310.00, decimals: 0, label: 'Iraqi Dinar', flag: '🇮🇶' },
    'ILS': { symbol: '₪', rate: 3.72, decimals: 2, label: 'Israeli New Shekel', flag: '🇮🇱' },

    // J - K
    'JMD': { symbol: 'J$ ', rate: 158.00, decimals: 2, label: 'Jamaican Dollar', flag: '🇯🇲' },
    'JPY': { symbol: '¥', rate: 155.50, decimals: 0, label: 'Japanese Yen', flag: '🇯🇵' },
    'JOD': { symbol: 'JD ', rate: 0.709, decimals: 3, label: 'Jordanian Dinar', flag: '🇯🇴' },
    'KZT': { symbol: '₸', rate: 495.00, decimals: 2, label: 'Kazakhstani Tenge', flag: '🇰🇿' },
    'KES': { symbol: 'KSh ', rate: 129.50, decimals: 2, label: 'Kenyan Shilling', flag: '🇰🇪' },
    'KWD': { symbol: 'KD ', rate: 0.31, decimals: 3, label: 'Kuwaiti Dinar', flag: '🇰🇼' },
    'KGS': { symbol: 'с ', rate: 86.50, decimals: 2, label: 'Kyrgyzstani Som', flag: '🇰🇬' },

    // L - M
    'LAK': { symbol: '₭ ', rate: 21900.00, decimals: 0, label: 'Lao Kip', flag: '🇱🇦' },
    'LBP': { symbol: 'L£ ', rate: 89500.00, decimals: 0, label: 'Lebanese Pound', flag: '🇱🇧' },
    'LSL': { symbol: 'L ', rate: 18.20, decimals: 2, label: 'Lesotho Loti', flag: '🇱🇸' },
    'LRD': { symbol: 'L$ ', rate: 195.00, decimals: 2, label: 'Liberian Dollar', flag: '🇱🇷' },
    'LYD': { symbol: 'LD ', rate: 4.85, decimals: 3, label: 'Libyan Dinar', flag: '🇱🇾' },
    'CHF': { symbol: 'CHF ', rate: 0.89, decimals: 2, label: 'Swiss Franc', flag: '🇨🇭' },
    'MGA': { symbol: 'Ar ', rate: 4600.00, decimals: 0, label: 'Malagasy Ariary', flag: '🇲🇬' },
    'MWK': { symbol: 'MK ', rate: 1735.00, decimals: 2, label: 'Malawian Kwacha', flag: '🇲🇼' },
    'MYR': { symbol: 'RM ', rate: 4.45, decimals: 2, label: 'Malaysian Ringgit', flag: '🇲🇾' },
    'MVR': { symbol: 'Rf ', rate: 15.45, decimals: 2, label: 'Maldivian Rufiyaa', flag: '🇲🇻' },
    'MRU': { symbol: 'UM ', rate: 39.80, decimals: 2, label: 'Mauritanian Ouguiya', flag: '🇲🇷' },
    'MUR': { symbol: 'Rs ', rate: 46.50, decimals: 2, label: 'Mauritian Rupee', flag: '🇲🇺' },
    'MXN': { symbol: 'Mex$', rate: 19.85, decimals: 2, label: 'Mexican Peso', flag: '🇲🇽' },
    'MDL': { symbol: 'L ', rate: 18.05, decimals: 2, label: 'Moldovan Leu', flag: '🇲🇩' },
    'MNT': { symbol: '₮ ', rate: 3450.00, decimals: 0, label: 'Mongolian Tögrög', flag: '🇲🇳' },
    'MAD': { symbol: 'MAD ', rate: 9.95, decimals: 2, label: 'Moroccan Dirham', flag: '🇲🇦' },
    'MZN': { symbol: 'MT ', rate: 63.90, decimals: 2, label: 'Mozambican Metical', flag: '🇲🇿' },
    'MMK': { symbol: 'K ', rate: 2100.00, decimals: 0, label: 'Myanmar Kyat', flag: '🇲🇲' },

    // N - P
    'NAD': { symbol: 'N$ ', rate: 18.20, decimals: 2, label: 'Namibian Dollar', flag: '🇳🇦' },
    'NPR': { symbol: 'NPR ', rate: 139.50, decimals: 2, label: 'Nepalese Rupee', flag: '🇳🇵' },
    'NZD': { symbol: 'NZ$', rate: 1.68, decimals: 2, label: 'New Zealand Dollar', flag: '🇳🇿' },
    'NIO': { symbol: 'C$ ', rate: 36.80, decimals: 2, label: 'Nicaraguan Córdoba', flag: '🇳🇮' },
    'NGN': { symbol: '₦', rate: 1680.00, decimals: 2, label: 'Nigerian Naira', flag: '🇳🇬' },
    'KPW': { symbol: '₩ ', rate: 900.00, decimals: 0, label: 'North Korean Won', flag: '🇰🇵' },
    'MKD': { symbol: 'den ', rate: 56.70, decimals: 2, label: 'Macedonian Denar', flag: '🇲🇰' },
    'NOK': { symbol: 'kr ', rate: 10.75, decimals: 2, label: 'Norwegian Krone', flag: '🇳🇴' },
    'OMR': { symbol: 'OMR ', rate: 0.385, decimals: 3, label: 'Omani Rial', flag: '🇴🇲' },
    'PKR': { symbol: 'PKR ', rate: 279.50, decimals: 2, label: 'Pakistani Rupee', flag: '🇵🇰' },
    'PAB': { symbol: 'B/. ', rate: 1.00, decimals: 2, label: 'Panamanian Balboa', flag: '🇵🇦' },
    'PGK': { symbol: 'K ', rate: 3.95, decimals: 2, label: 'Papua New Guinean Kina', flag: '🇵🇬' },
    'PYG': { symbol: '₲', rate: 7800.00, decimals: 0, label: 'Paraguayan Guaraní', flag: '🇵🇾' },
    'PEN': { symbol: 'S/ ', rate: 3.76, decimals: 2, label: 'Peruvian Sol', flag: '🇵🇪' },
    'PHP': { symbol: '₱', rate: 58.20, decimals: 2, label: 'Philippine Peso', flag: '🇵🇭' },
    'PLN': { symbol: 'zł ', rate: 3.98, decimals: 2, label: 'Polish Złoty', flag: '🇵🇱' },

    // Q - S
    'QAR': { symbol: 'QAR ', rate: 3.64, decimals: 2, label: 'Qatari Riyal', flag: '🇶🇦' },
    'RON': { symbol: 'lei ', rate: 4.58, decimals: 2, label: 'Romanian Leu', flag: '🇷🇴' },
    'RUB': { symbol: '₽', rate: 91.50, decimals: 2, label: 'Russian Ruble', flag: '🇷🇺' },
    'RWF': { symbol: 'FRw ', rate: 1380.00, decimals: 0, label: 'Rwandan Franc', flag: '🇷🇼' },
    'WST': { symbol: 'WS$ ', rate: 2.74, decimals: 2, label: 'Samoan Tālā', flag: '🇼🇸' },
    'STN': { symbol: 'Db ', rate: 22.50, decimals: 2, label: 'São Tomé Dobra', flag: '🇸🇹' },
    'SAR': { symbol: 'SAR ', rate: 3.75, decimals: 2, label: 'Saudi Riyal', flag: '🇸🇦' },
    'RSD': { symbol: 'din ', rate: 108.00, decimals: 2, label: 'Serbian Dinar', flag: '🇷🇸' },
    'SCR': { symbol: 'SR ', rate: 14.20, decimals: 2, label: 'Seychellois Rupee', flag: '🇸🇨' },
    'SLE': { symbol: 'Le ', rate: 22.80, decimals: 2, label: 'Sierra Leonean Leone', flag: '🇸🇱' },
    'SGD': { symbol: 'S$', rate: 1.34, decimals: 2, label: 'Singapore Dollar', flag: '🇸🇬' },
    'SBD': { symbol: 'SI$ ', rate: 8.45, decimals: 2, label: 'Solomon Islands Dollar', flag: '🇸🇧' },
    'SOS': { symbol: 'Ssh ', rate: 571.00, decimals: 2, label: 'Somali Shilling', flag: '🇸🇴' },
    'ZAR': { symbol: 'R ', rate: 18.20, decimals: 2, label: 'South African Rand', flag: '🇿🇦' },
    'KRW': { symbol: '₩', rate: 1385.00, decimals: 0, label: 'South Korean Won', flag: '🇰🇷' },
    'SSP': { symbol: 'SS£ ', rate: 1300.00, decimals: 2, label: 'South Sudanese Pound', flag: '🇸🇸' },
    'LKR': { symbol: 'Rs ', rate: 298.00, decimals: 2, label: 'Sri Lankan Rupee', flag: '🇱🇰' },
    'SDG': { symbol: 'SDG ', rate: 601.00, decimals: 2, label: 'Sudanese Pound', flag: '🇸🇩' },
    'SRD': { symbol: 'Sr$ ', rate: 35.20, decimals: 2, label: 'Surinamese Dollar', flag: '🇸🇷' },
    'SEK': { symbol: 'kr ', rate: 10.45, decimals: 2, label: 'Swedish Krona', flag: '🇸🇪' },
    'SYP': { symbol: 'LS ', rate: 13000.00, decimals: 0, label: 'Syrian Pound', flag: '🇸🇾' },

    // T - Z
    'TJS': { symbol: 'SM ', rate: 10.65, decimals: 2, label: 'Tajikistani Somoni', flag: '🇹🇯' },
    'TZS': { symbol: 'TSh ', rate: 2650.00, decimals: 0, label: 'Tanzanian Shilling', flag: '🇹🇿' },
    'THB': { symbol: '฿', rate: 34.50, decimals: 2, label: 'Thai Baht', flag: '🇹🇭' },
    'TOP': { symbol: 'T$ ', rate: 2.38, decimals: 2, label: 'Tongan Paʻanga', flag: '🇹🇴' },
    'TTD': { symbol: 'TT$ ', rate: 6.78, decimals: 2, label: 'Trinidad & Tobago Dollar', flag: '🇹🇹' },
    'TND': { symbol: 'DT ', rate: 3.12, decimals: 3, label: 'Tunisian Dinar', flag: '🇹🇳' },
    'TRY': { symbol: '₺', rate: 34.25, decimals: 2, label: 'Turkish Lira', flag: '🇹🇷' },
    'TMT': { symbol: 'm ', rate: 3.50, decimals: 2, label: 'Turkmenistan Manat', flag: '🇹🇲' },
    'UGX': { symbol: 'USh ', rate: 3670.00, decimals: 0, label: 'Ugandan Shilling', flag: '🇺🇬' },
    'UAH': { symbol: '₴', rate: 41.20, decimals: 2, label: 'Ukrainian Hryvnia', flag: '🇺🇦' },
    'AED': { symbol: 'AED ', rate: 3.67, decimals: 2, label: 'UAE Dirham', flag: '🇦🇪' },
    'GBP': { symbol: '£', rate: 0.78, decimals: 2, label: 'Pound Sterling', flag: '🇬🇧' },
    'UYU': { symbol: '$U ', rate: 41.50, decimals: 2, label: 'Uruguayan Peso', flag: '🇺🇾' },
    'UZS': { symbol: 'UZS ', rate: 12800.00, decimals: 0, label: 'Uzbekistani Som', flag: '🇺🇿' },
    'VUV': { symbol: 'VT ', rate: 120.00, decimals: 0, label: 'Vanuatu Vatu', flag: '🇻🇺' },
    'VES': { symbol: 'Bs. ', rate: 45.00, decimals: 2, label: 'Venezuelan Bolívar', flag: '🇻🇪' },
    'VND': { symbol: '₫', rate: 25400.00, decimals: 0, label: 'Vietnamese Đồng', flag: '🇻🇳' },
    'YER': { symbol: 'YR ', rate: 250.00, decimals: 2, label: 'Yemeni Rial', flag: '🇾🇪' },
    'ZMW': { symbol: 'ZK ', rate: 27.50, decimals: 2, label: 'Zambian Kwacha', flag: '🇿🇲' },
    'ZiG': { symbol: 'ZiG ', rate: 26.80, decimals: 2, label: 'Zimbabwe Gold', flag: '🇿🇼' }
};

// 1-to-1 Mapping for ALL 195 Countries
const WORLD_COUNTRY_MAP = {
    // 1 - 20
    'afghanistan': 'AFN',
    'albania': 'ALL',
    'algeria': 'DZD',
    'andorra': 'EUR',
    'angola': 'AOA',
    'antigua and barbuda': 'XCD', 'antigua': 'XCD', 'barbuda': 'XCD',
    'argentina': 'ARS',
    'armenia': 'AMD',
    'australia': 'AUD', 'aus': 'AUD', 'au': 'AUD',
    'austria': 'EUR',
    'azerbaijan': 'AZN',
    'bahamas': 'BSD',
    'bahrain': 'BHD',
    'bangladesh': 'BDT', 'bd': 'BDT',
    'barbados': 'BBD',
    'belarus': 'BYN',
    'belgium': 'EUR',
    'belize': 'BZD',
    'benin': 'XOF',
    'bhutan': 'BTN',

    // 21 - 40
    'bolivia': 'BOB',
    'bosnia and herzegovina': 'BAM', 'bosnia': 'BAM',
    'botswana': 'BWP',
    'brazil': 'BRL', 'brasil': 'BRL',
    'brunei': 'BND',
    'bulgaria': 'BGN',
    'burkina faso': 'XOF',
    'burundi': 'BIF',
    'cabo verde': 'CVE', 'cape verde': 'CVE',
    'cambodia': 'KHR',
    'cameroon': 'XAF',
    'canada': 'CAD', 'can': 'CAD',
    'central african republic': 'XAF', 'car': 'XAF',
    'chad': 'XAF',
    'chile': 'CLP',
    'china': 'CNY', 'prc': 'CNY',
    'colombia': 'COP',
    'comoros': 'KMF',
    'congo': 'XAF', 'republic of the congo': 'XAF',
    'costa rica': 'CRC',

    // 41 - 60
    "côte d'ivoire": 'XOF', "cote d'ivoire": 'XOF', 'ivory coast': 'XOF',
    'croatia': 'EUR',
    'cuba': 'CUP',
    'cyprus': 'EUR',
    'czechia': 'CZK', 'czech republic': 'CZK',
    'dr congo': 'CDF', 'democratic republic of the congo': 'CDF',
    'denmark': 'DKK',
    'djibouti': 'DJF',
    'dominica': 'XCD',
    'dominican republic': 'DOP',
    'ecuador': 'USD',
    'egypt': 'EGP',
    'el salvador': 'USD',
    'equatorial guinea': 'XAF',
    'eritrea': 'ERN',
    'estonia': 'EUR',
    'eswatini': 'SZL', 'swaziland': 'SZL',
    'ethiopia': 'ETB',
    'fiji': 'FJD',
    'finland': 'EUR',

    // 61 - 80
    'france': 'EUR',
    'gabon': 'XAF',
    'gambia': 'GMD',
    'georgia': 'GEL',
    'germany': 'EUR', 'deutschland': 'EUR',
    'ghana': 'GHS',
    'greece': 'EUR',
    'grenada': 'XCD',
    'guatemala': 'GTQ',
    'guinea': 'GNF',
    'guinea-bissau': 'XOF',
    'guyana': 'GYD',
    'haiti': 'HTG',
    'honduras': 'HNL',
    'hungary': 'HUF',
    'iceland': 'ISK',
    'india': 'INR', 'bharat': 'INR', 'ind': 'INR', 'in': 'INR',
    'indonesia': 'IDR',
    'iran': 'IRR',
    'iraq': 'IQD',

    // 81 - 100
    'ireland': 'EUR',
    'israel': 'ILS',
    'italy': 'EUR', 'italia': 'EUR',
    'jamaica': 'JMD',
    'japan': 'JPY', 'jpn': 'JPY', 'jp': 'JPY',
    'jordan': 'JOD',
    'kazakhstan': 'KZT',
    'kenya': 'KES',
    'kiribati': 'AUD',
    'kuwait': 'KWD',
    'kyrgyzstan': 'KGS',
    'laos': 'LAK',
    'latvia': 'EUR',
    'lebanon': 'LBP',
    'lesotho': 'LSL',
    'liberia': 'LRD',
    'libya': 'LYD',
    'liechtenstein': 'CHF',
    'lithuania': 'EUR',
    'luxembourg': 'EUR',

    // 101 - 120
    'madagascar': 'MGA',
    'malawi': 'MWK',
    'malaysia': 'MYR',
    'maldives': 'MVR',
    'mali': 'XOF',
    'malta': 'EUR',
    'marshall islands': 'USD',
    'mauritania': 'MRU',
    'mauritius': 'MUR',
    'mexico': 'MXN', 'mex': 'MXN',
    'micronesia': 'USD',
    'moldova': 'MDL',
    'monaco': 'EUR',
    'mongolia': 'MNT',
    'montenegro': 'EUR',
    'morocco': 'MAD',
    'mozambique': 'MZN',
    'myanmar': 'MMK', 'burma': 'MMK',
    'namibia': 'NAD',
    'nauru': 'AUD',

    // 121 - 140
    'nepal': 'NPR', 'npl': 'NPR', 'np': 'NPR',
    'netherlands': 'EUR', 'holland': 'EUR',
    'new zealand': 'NZD', 'nz': 'NZD',
    'nicaragua': 'NIO',
    'niger': 'XOF',
    'nigeria': 'NGN',
    'north korea': 'KPW',
    'north macedonia': 'MKD', 'macedonia': 'MKD',
    'norway': 'NOK',
    'oman': 'OMR',
    'pakistan': 'PKR', 'pak': 'PKR', 'pk': 'PKR',
    'palau': 'USD',
    'palestine': 'ILS',
    'panama': 'PAB',
    'papua new guinea': 'PGK',
    'paraguay': 'PYG',
    'peru': 'PEN',
    'philippines': 'PHP', 'ph': 'PHP',
    'poland': 'PLN',
    'portugal': 'EUR',

    // 141 - 160
    'qatar': 'QAR',
    'romania': 'RON',
    'russia': 'RUB', 'russian federation': 'RUB', 'ru': 'RUB',
    'rwanda': 'RWF',
    'saint kitts and nevis': 'XCD', 'saint kitts': 'XCD', 'nevis': 'XCD',
    'saint lucia': 'XCD',
    'saint vincent and the grenadines': 'XCD', 'saint vincent': 'XCD',
    'samoa': 'WST',
    'san marino': 'EUR',
    'são tomé and príncipe': 'STN', 'sao tome and principe': 'STN', 'sao tome': 'STN',
    'saudi arabia': 'SAR', 'saudi': 'SAR', 'ksa': 'SAR',
    'senegal': 'XOF',
    'serbia': 'RSD',
    'seychelles': 'SCR',
    'sierra leone': 'SLE',
    'singapore': 'SGD', 'sg': 'SGD',
    'slovakia': 'EUR',
    'slovenia': 'EUR',
    'solomon islands': 'SBD',
    'somalia': 'SOS',

    // 161 - 180
    'south africa': 'ZAR', 'za': 'ZAR',
    'south korea': 'KRW', 'korea': 'KRW', 'kr': 'KRW', 'kor': 'KRW',
    'south sudan': 'SSP',
    'spain': 'EUR', 'espana': 'EUR',
    'sri lanka': 'LKR', 'lanka': 'LKR',
    'sudan': 'SDG',
    'suriname': 'SRD',
    'sweden': 'SEK',
    'switzerland': 'CHF', 'swiss': 'CHF',
    'syria': 'SYP',
    'tajikistan': 'TJS',
    'tanzania': 'TZS',
    'thailand': 'THB', 'th': 'THB',
    'timor-leste': 'USD', 'east timor': 'USD',
    'togo': 'XOF',
    'tonga': 'TOP',
    'trinidad and tobago': 'TTD', 'trinidad': 'TTD', 'tobago': 'TTD',
    'tunisia': 'TND',
    'türkiye': 'TRY', 'turkey': 'TRY', 'tr': 'TRY',
    'turkmenistan': 'TMT',

    // 181 - 195
    'tuvalu': 'AUD',
    'uganda': 'UGX',
    'ukraine': 'UAH', 'ua': 'UAH',
    'united arab emirates': 'AED', 'uae': 'AED', 'dubai': 'AED', 'ae': 'AED',
    'united kingdom': 'GBP', 'uk': 'GBP', 'great britain': 'GBP', 'britain': 'GBP', 'england': 'GBP', 'gb': 'GBP',
    'united states': 'USD', 'united states of america': 'USD', 'usa': 'USD', 'us': 'USD', 'america': 'USD',
    'uruguay': 'UYU',
    'uzbekistan': 'UZS',
    'vanuatu': 'VUV',
    'vatican city': 'EUR', 'vatican': 'EUR',
    'venezuela': 'VES',
    'vietnam': 'VND', 'viet nam': 'VND', 'vn': 'VND',
    'yemen': 'YER',
    'zambia': 'ZMW',
    'zimbabwe': 'ZiG'
};

/**
 * Universal Zero-Error Country Resolver
 */
function resolveCountryCurrencyCode(countryName) {
    if (!countryName || typeof countryName !== 'string') return 'USD';
    const clean = countryName.trim().toLowerCase();

    // 1. Direct match in 195 country dictionary
    if (WORLD_COUNTRY_MAP[clean]) {
        return WORLD_COUNTRY_MAP[clean];
    }

    // 2. Direct ISO Currency Code check
    const upperCode = countryName.trim().toUpperCase();
    if (WORLD_CURRENCY_RATES[upperCode]) {
        return upperCode;
    }

    // 3. Substring & Fuzzy search
    for (let key in WORLD_COUNTRY_MAP) {
        if (clean.includes(key) || key.includes(clean)) {
            return WORLD_COUNTRY_MAP[key];
        }
    }

    // 4. Fallback gracefully to USD
    return 'USD';
}

/**
 * Format USD value to converted Target Currency with zero errors and proper decimal handling.
 */
function formatWorldCurrency(usdVal, currencyCode) {
    const rawVal = parseFloat(usdVal);
    const validUsd = isNaN(rawVal) ? 0.0 : rawVal;

    const code = currencyCode && WORLD_CURRENCY_RATES[currencyCode] ? currencyCode : 'USD';
    const info = WORLD_CURRENCY_RATES[code];
    const converted = validUsd * info.rate;

    let formatted = '';
    if (info.decimals === 0) {
        formatted = Math.round(converted).toLocaleString();
    } else {
        formatted = converted.toLocaleString(undefined, {
            minimumFractionDigits: info.decimals,
            maximumFractionDigits: info.decimals
        });
    }

    return `${info.symbol}${formatted}`;
}
