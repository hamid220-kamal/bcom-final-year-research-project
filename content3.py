"""Additional content for Glossary and Statistical Appendices."""

GLOSSARY = {
    "Aggregate Turnover": "The total value of all taxable supplies (excluding the value of inward supplies on which tax is payable by a person on reverse charge basis), exempt supplies, exports of goods or services or both, and inter-State supplies of persons having the same PAN, computed on an all-India basis but excludes CGST, SGST, UTGST, IGST, and cess.",
    "B2B (Business to Business)": "Transactions between two registered business entities. In GST, B2B invoices are essential for the buyer to claim Input Tax Credit.",
    "B2C (Business to Consumer)": "Transactions between a registered business and an unregistered end consumer. The consumer cannot claim any Input Tax Credit for the tax paid.",
    "Casual Taxable Person": "A person who occasionally undertakes transactions involving supply of goods or services or both in the course or furtherance of business, whether as principal, agent or in any other capacity, in a State or a Union territory where they have no fixed place of business.",
    "Cess": "A tax levied on tax. Under GST, a Compensation Cess is levied on certain notified luxury or demerit goods (like pan masala, tobacco products, and automobiles) to compensate the states for any revenue loss arising from the transition to GST.",
    "CGST (Central Goods and Services Tax)": "The component of GST levied by the Central Government on the intra-state supply of goods and services. Revenue collected under CGST accrues to the Consolidated Fund of India.",
    "Composition Scheme": "A simpler alternative to the regular GST scheme designed to reduce the compliance burden for small taxpayers. Eligible businesses (turnover up to Rs. 1.5 Crores) pay fixed-rate tax on turnover but cannot claim ITC or collect tax from customers.",
    "Destination-Based Tax": "A principle where the tax is levied at the point of consumption rather than the point of origin. Under GST, the revenue accrues to the state where the goods or services are finally consumed.",
    "E-Way Bill": "An electronic document generated on the GST portal evidencing the movement of goods. It is mandatory for the inter-state or intra-state movement of goods exceeding Rs. 50,000 in value, ensuring tax compliance during transit.",
    "Exempt Supply": "A supply of goods or services or both which attracts a nil rate of tax or which may be wholly exempt from tax under Section 11, or under Section 6 of the IGST Act, and includes a non-taxable supply. Examples include fresh milk and unmilled grains.",
    "GSTIN (Goods and Services Tax Identification Number)": "A 15-digit, PAN-based unique identification number allotted to every registered person under GST. It replaces earlier registrations like VAT TIN, CST form, and Service Tax numbers.",
    "GSTR-1": "A monthly or quarterly return that contains details of all outward supplies (sales) made by a registered taxpayer. This form serves as the foundational data for the auto-population of the buyer's ITC records.",
    "GSTR-2A / 2B": "Auto-populated, view-only dynamic and static statements respectively, generated for a registered recipient. They display the details of inward supplies based on the outward supply details filed by their suppliers in GSTR-1.",
    "GSTR-3B": "A simplified summary return filed monthly (or quarterly under QRMP) declaring the tax liability for a given period. It involves the calculation of total tax payable on sales, deduction of available ITC, and payment of the net tax balance.",
    "GSTR-4": "An annual return to be filed by taxpayers who have opted for the Composition Scheme under GST. Prior to 2019-20, it was filed quarterly.",
    "HSN (Harmonized System of Nomenclature) Code": "An internationally recognized, multi-purpose, six-digit product nomenclature system developed by the World Customs Organization. In India, it is expanded to 8 digits for detailed classification of goods and determining specific GST rates.",
    "IGST (Integrated Goods and Services Tax)": "The component of GST levied by the Central Government on all inter-state supplies (including imports). The ITC of IGST can be used to pay IGST, CGST, and SGST liabilities in that order.",
    "Input Tax Credit (ITC)": "The mechanism by which a registered taxpayer can reduce the tax they have already paid on inputs (purchases) from the tax they are liable to pay on outputs (sales), thereby avoiding a cascade of taxes.",
    "Input Tax": "In relation to a registered person, the IGST, CGST, SGST, or UTGST charged on any supply of goods or services or both made to him and includes tax payable under reverse charge, and tax on imports.",
    "Inward Supply": "Receipt of goods or services or both whether by purchase, acquisition or any other means, with or without consideration.",
    "Outward Supply": "Supply of goods or services or both, whether by sale, transfer, barter, exchange, licence, rental, lease or disposal, made or agreed to be made by a person in the course or furtherance of business.",
    "PAN (Permanent Account Number)": "A 10-character alphanumeric identifier issued by the Indian Income Tax Department. Possession of a valid PAN is a mandatory pre-requisite for obtaining GST registration.",
    "QRMP Scheme (Quarterly Return Monthly Payment)": "A scheme introduced to ease compliance for small taxpayers (aggregate annual turnover up to Rs. 5 Crores). It allows them to file their GSTR-1 and GSTR-3B returns quarterly while paying their estimated tax dues monthly.",
    "Reverse Charge Mechanism (RCM)": "A scenario where the liability to pay tax rests on the recipient of the supply of goods or services instead of the supplier. Common examples include services provided by a Goods Transport Agency (GTA) or an advocate.",
    "SAC (Service Accounting Code)": "A unified code system adopted by the Central Board of Indirect Taxes and Customs (CBIC) for the classification, administration, and measurement of services under the GST regime.",
    "SGST (State Goods and Services Tax)": "The component of GST levied on an intra-state supply of goods and services by the respective State Government. It mirrors the provisions of the CGST Act.",
    "Supply": "The taxable event under GST. It includes all forms of supply of goods or services or both such as sale, transfer, barter, exchange, license, rental, lease or disposal made or agreed to be made for a consideration by a person in the course or furtherance of business.",
    "Tax Invoice": "A commercial instrument issued by a registered supplier to a recipient containing specific details like GSTIN of both parties, HSN code, value of supply, and tax charged. It is the primary document required for claiming ITC.",
    "UTGST (Union Territory Goods and Services Tax)": "The tax levied on the intra-Union Territory supply of goods or services or both in Union Territories without a legislature (e.g., Andaman and Nicobar Islands, Lakshadweep, Dadra and Nagar Haveli, Daman and Diu, and Chandigarh)."
}

STAT_APPENDIX = [
    {
        "title": "Sector-Wise Average Compliance Cost Analysis (N=50)",
        "desc": "Detailed breakdown of the monthly monetary and time-equivalent costs incurred by different business categories for GST compliance in Shadnagar.",
        "headers": ["Business Sector", "Accountant Fee", "Software/Internet", "Time Cost (Est.)", "Total Monthly Burden"],
        "rows": [
            ["Retail Grocery", "Rs. 1,200", "Rs. 300", "Rs. 800", "Rs. 2,300"],
            ["Textile/Apparel", "Rs. 1,500", "Rs. 400", "Rs. 1,000", "Rs. 2,900"],
            ["Electronics Repair", "Rs. 1,800", "Rs. 500", "Rs. 1,200", "Rs. 3,500"],
            ["Hardware/Paints", "Rs. 1,600", "Rs. 600", "Rs. 1,100", "Rs. 3,300"],
            ["Food/Restaurant", "Rs. 1,500", "Rs. 300", "Rs. 1,000", "Rs. 2,800"],
            ["Manufacturing", "Rs. 2,200", "Rs. 600", "Rs. 1,500", "Rs. 4,300"]
        ]
    },
    {
        "title": "Composition Scheme vs Regular Scheme Demographics",
        "desc": "Distribution of the 50 surveyed sole traders among the two primary GST schemes cross-tabulated with their annual turnover brackets.",
        "headers": ["Annual Turnover", "Regular Scheme", "Composition Scheme", "Total Traders"],
        "rows": [
            ["Below Rs. 20 Lakh", "0", "5", "5 (10%)"],
            ["Rs. 20 - 40 Lakh", "2", "15", "17 (34%)"],
            ["Rs. 40 - 75 Lakh", "5", "10", "15 (30%)"],
            ["Rs. 75 - 150 Lakh", "4", "5", "9 (18%)"],
            ["Above Rs. 1.5 Cr", "4", "0", "4 (8%)"],
            ["Total", "15 (30%)", "35 (70%)", "50 (100%)"]
        ]
    },
    {
        "title": "ITC Mis-match and Denial Experiences",
        "desc": "Analysis of the 15 Regular Scheme traders who are eligible for ITC, tracking the frequency of ITC denial due to supplier non-compliance.",
        "headers": ["ITC Experience", "Number of Traders", "Percentage of Regular"],
        "rows": [
            ["Seamless ITC (No issues)", "4", "26.7%"],
            ["Occasional mismatch (Resolved)", "6", "40.0%"],
            ["Frequent mismatch (Lost credit)", "5", "33.3%"],
            ["Received formal ITC notice", "2", "13.3%"]
        ]
    }
]
