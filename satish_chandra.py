def create_book(kg, topic_id):
    # 1. Create the root "Brick" node (Topic)
    # topic_id = kg.create_topic("BRICKS")
    
    # 2. Create the Book node and link it to the Topic
    book_id = kg.create_book(
        "HISTORY of Architecture and Ancient Building Materials in India Part I & II",
        """History of Architecture and Ancient 
            Building Matenals in India" consists of two 
            parts, Thafirstpart deals with tbs architecture of 
            India and the second part is about the ancient 
            building materials Theaim of fjwjjiore* ta not to go 
            into detea about the arahfteetomltostdry of India 
            but to give an impression aha te^reness about 
            tfv. a rt^iflCfLtfrtrtus eu*i*d in the ancfent penod 
            and how it UiTtshto during the ctifferem rulers 
            who tnvaded India 

            The second pafl deals wift the building 
            materials used ln4e ancient period, which is a 
            unique contribution. It'provides the information 
            about the materials specifically the natural 
            polymers, used in the. ancient period, and the 
            technique of their application. Most Interesting part 
            Is the scientific explanations and the narration's 
            about the mechanisms involved in the interactions 
            of the ingredients used in the construction, which 
            enhanced the durability properties of toe structure. 
            The materials ascribed are not only from India, 
            some plasters and mortar compositions used in 
            the other part of the worid are also described. It 
            is a very valuable and comprehensive piece of 
            work and will be a guide book for the practicing 
            engineers. restorers, conservator’s, 
            archaeologists, historians and also for the people 
            in general interested in the building materials 

            The book carries Foreword by Ingval 
            Maxwell, DA Dun, RIBA, FRIAS, AABC, FSA Scot, 
            Director, Technical Conservation, Research and 
            Education Division Historic Scotland, Edinburgh, 
            Scotland and R.S. Bisht Director in the 
            Archaeological Survey of the Government of India, 
            at New Delhi. 

            The prime objective of this remarkable book 
            is about the chemistry & analysis of the materials 
            used in our ancient monuments, today standing 
            as a symbol of our cultural heritage, after 
            thousands of years. A need was felt to have an 
            indepth study of chemistry of the ancient building 
            materials used in the construction of these ancient 
            monuments in their relation, as to the chemistry of 
            cement and its binding properties and durability 
            of structures. 


            History of Architecture 
            and 

            Ancient Building Materials 
            in India Part 1 & II 

            (in single volume) 


            by 

            SAT I SI I CHANDRA """
    )
    kg.create_relationship(topic_id, "HAS_BOOK", book_id)
    
    # 3. Create a Chapter node for "BRICKS" and link it to the Book
    chapter_id = kg.create_chapter(
        "BRICKS",
        "Bricks for building construction were of two types. The earliest use of the \
            molded bricks was after baking them in the sun. Later, the technique was \
            developed to burn them at high temperature. The former type of bricks was \
            cheap and simple to make whereas the latter were complicated due to the \
            burning process and thereby were expensive. "
    )
    kg.create_relationship(book_id, "HAS_CHAPTER", chapter_id)
    
    # 4. Create a Section node for "3.1 Sunbaked Bricks" and link it to the Chapter
    section_id = kg.create_section(
        "3.1 Sunbaked Bricks",
        ("""The precise history of sunbaked bricks is not known as to when these were 
            developed and used for the first time. However, the earliest use found is at 
            Dholavira , which has emerged as a major Harappan city, remarkable for its 
            exquisitive planning, monumental structures, aesthetic architecture and 
            wonderful water management system [Joshi and Bisht, 1994]. According 
            to Archaeological Survey of India there were seven cultural stages. The 
            first settlers who came to Dholavira seems to be well trained in the building 
            techniques. They have constructed a formidable fortification (as thick as 1 
            meters at the base round the settlement). The houses were made of the mud 
            bricks of standardized sizes providing the ratio 4:2:1. (Figure 3.1) 

            Mud bricks were also used in the construction of Indraprastha, a village 
            of Pandava’s (Mahabharat). It is clearly seen from the ruins of the village 
            (Figure 3.2). Location of this village is at the place of Red Fort, Delhi (see 
            Indo Aryan Architect, Part I). 

            Bricks are actually made from the soil and not the clay. Clay is a part of 
            the soil, which has the bonding property. Making bricks looks very simple, 
            but in fact it is not. There are many factors, which are to be taken into 
            consideration for making them.""")
    )
    kg.create_relationship(chapter_id, "HAS_SECTION", section_id)
    
    # 5. Create a Subsection node for "3.1.1 Selection of Soil and Brick Making Technique"
    #    and link it to the Section node
    subsection_id = kg.create_subsection(
        "3.1.1 Selection of Soil and Brick Making Technique",
        ("""The bricks should be made of specially selected soils otherwise they are 
            not durable. For example bricks made from sandy or pebbly clay or from 
            fine gravel, are heavy, and are not durable. It has bad bonding and are 
            washed away in the rain. There are many kinds of clayey materials suitable for
            making the bricks. They may be almost pure and plastic clays white and chalky or
            of red clay, products obtained by the natural decay and disintegration of igneous rock 
            and shale, or they may be wind blown


            300 

            History of Architecture and Ancient 
            Building Materials in India Part-1! 

            materials with significant amount of sand and silt. These can be white and 
            chalky clays or even red clays. 

            Bricks made with this type of clay are smooth, are easy to work with 
            and have good bond. Furthermore these are not heavy. 

            The best materials for making the bricks are latter types, which contains 
            up to 30% of sand and silt. The presence of sand in particular reduces the 
            shrinkage that occurs when the plastic clays are burned. Clays are basically 
            composed of hydrated oxides of aluminium and iron, and hydrated silicates 
            of aluminium, but may also contain calcium carbonate, gypsum, pyrites 
            etc. Gypsum is undesirable as it subsequently leads to the efflorescence on 
            the face of the brickwork, and may even cause the bricks themselves to 
            crack. The local builders have adequate knowledge and are careful in 
            selection of the clay. Gypsum occurs in the crystal form, often in nodules, 
            and can be felt by hand. 

            The soil within a foot or so from the surface is used. It is prepared wtih
            the addition of leaves, or dry straw (Chopped stems of cereals, Bhusa) and
            ample of water. It is thoroughly mixed and is left exposed for some time
            depending upon the weather and the time of the year. This should be kneaded
            in between to ensure thorough mixing and compaction. Which produces
            bricks of high durability. During this time the leaves get rotten. The humus
            from the leaves gives plasticity to the clay and the fibers provides
            reinforcement. Any nodules of gypsum are removed at the same time. 

            The bricks are molded in the wooden frames by casting the soil 
            prepared and beating it with wooden clubs (Figure 3.3). These when 
            sufficiently dried so that they will not be deformed by movement are put 
            over each other making open space between them like checker. This way, 
            the air passes through them and drying takes place more uniformly. The 
            bricks also dry faster. It is shown in the Figure 3.4. These are left for sun 
            drying for a couple of weeks. When the bricks are dried these become 
            stabilized, as there will be no cracks which used to come due to the shrinkage 
            of the mud when the water evaporates. There will also not be delamination 
            cracks, which come due to the movement of the mud during drying. These 
            bricks are used for making the walls and the mortar used for joining them 
            is made of the mud and the organics. When the wall is finished it is plastered 
            with the mortar made of mud and organic. Thus it becomes a monolithic 
            structure without cracks. The houses constructed with the sun-baked bricks 
            are durable and stable compared to those made only witli the mud. 



            Bricks

            Bricks should he made in (he spring or autumn, so that they may dry 
            uniformly- Those made in the summer are not of good quality. The bricks 
            dry very fast on the surface due to the high temperature prevailing in the 
            summer lime while the interior of the brick is still wet. This non-uniform 
            drying cause shrinkage in the bricks and develops cracks. The bricks loose 
            strength. The bricks should be dried slowly and uniformly. Older are the 
            bricks better is the service life. 

            When undried fresh bricks are used in a wall, the stucco covering stiffens 
            and hardens into a permanent mass, but the bricks settle and cannot keep 
            the same height as the stucco, the motion caused by their shrinking prevents 
            them from adhering to it, and they are separated. Hence the stucco, no 
            longer joined to the core of the wall, cannot stand by itself because it is too 
            thin: it breaks off, and their settling may perhaps ruin the walls themselves. 


            RM 118935

            Figure 3.1 North gate showing the use of mud bricks at Dholavira, Harappan
            City. [Joshi and Bisht, 1994]. 











            302 


            History of Architecture ami Ancient 
            Building Materials in India Part-II



            Figure 3.2 : Ruins of Indraprastha, Delhi, cir. 1500 B.C, [India Prospective 
            July 1996]. 



            Figure 3.3 : Making of mud bricks , Lucknow, India [Photo. Chandra , 1999]. 











            Bricks 


            303 



            Figure 3.4: Mud bricks are cast and piled for sun drying, Lucknow, India 
            [Photo, Chandra, 1999]. 

            Sun dried earth bricks usually hand made are becoming common in 
            rural part. The bricks are larger than the kiln fired bricks. However there is 
            no hard and fast rule and these do not conform to any standard size. Sun 
            dried bricks usually make stronger walls than those made only using earth. 

            The earliest use of mud bricks is in the construction of fortification 
            around the settlement at Dholavira. It is a city of the Bronze Age, situated 
            in the island of Khadir in the Great Rann of Kachchh in Gujarat. It was one 
            of the largest settlements of Harrappan civilization. The houses were made 
            of the molded mud bricks of standardized sizes providing the ratio 4:2:1. 
""")
    )
    kg.create_relationship(section_id, "HAS_SUBSECTION", subsection_id)

    section_id = kg.create_section(
        "3.2 Burnt Bricks",
        ("""The history of the use of burnt bricks goes back to the Indus Valley 
            Civilization cir. 2500 B.C. One of the evidence of the use of burnt bricks is 
            found at Mohenjo-daro; a city of Indus Valley Civilization (cir. 2300 B.C). 
            Most of Mohenjo-Daro was built of burnt bricks. There is massive mud 
            filled brick embankment, and on its summit are the remains of seveial 
            impressive structures, the most prominent of which is called “Great Bath 
            (Figure 3.5). The pool is surrounded by a paved courtyard, made of bricks 
            and made watertight by bitumen.

            Another evidence of the use of burnt bricks can be seen from the remains
            of a kiln excavated at Lothal, in Ahemdabad and dates back to cir. 2000
            B.C. [Archaeological Survey of India]. The Lothal culture was similar to  





            304 


            History of Architecture and Ancient 
            Building Materials in India Part-H 


            the culture of Harappa and Mohenjo-Daro. This confirms that the builders 
            were well versed with the technology of making and burning the bricks in 
            large scale in that period. """)
    )
    kg.create_relationship(chapter_id, "HAS_SECTION", section_id)

    # create subsection
    subsection_id = kg.create_subsection(
        "3.2.1 Burning of the Bricks",
        ("""The colour and the texture of the brick depends upon the iron oxide 
            impurities in the clay and the condition of firing. The majority of clays for 
            brick making, however, bum to a red colour when fired at between 900 to 
            1OOO °C. in an oxidizing atmosphere. Beyond this temperature the colour 
            often changes to darker red or purple, then grey at 1200 °C. In an reducing 
            atmosphere in which the supply of oxygen is restricted or cut off, for example 
            by reducing the draught through the kilns. Purple-brown'or bluish bricks, 
            often with black colours are produced. The effect of a high iron content in 
            the clay is to produce ferric oxide in an oxidizing atmosphere, making the 
            brick salmon pink in colour at 900 °C, and darker red or reddish brown at
            1100 °C, and ferrous oxide and ferrosic oxide in a reducing atmosphere 
            making a bluish brick. 

            The bricks made as described in Section 3.1 are laid down flat on the
            ground to dry for a few days to dry and to get some green strength. Later
            they are stacked on edge for some days, after which they are burnt. The
            temperature of burning is about 950 °C. 



            Figure 3.5 : Mohenjo-Daro , the Great Bath , Harrappan culture c. 2300 to 1750 
            B.C. (from Craven, R.C; A Concise History of Indian Art , Vikas 
            Publishing House , New Delhi , 1979, 13). 


            Bricks 


            305 



            Figure 3.6 : Bricks are piled for burning, Lucknow, [Photo Chandra, 1999]. 



            Figure 3.7 : Burning of the Bricks, Lucknow , [Photo, Chandra, 1999]










            306 


            Figure 3.8 : A brick kiln excavated at Lothal, Ahemdabad, India; c. 
            B.C.[ASI]. 



            Figure 3.9: Fuel used for burning the bricks, Lucknow,[Photo, Chandra, 1999]. 





            307 



            Figure 3.10 : Round down draft kiln for burning the bricks, Lucknow [Photo, 
            Chandra 1999]. 

            Bricks are burnt either in heaps or clamps “ Open Bhatta ” or in specially 
            constructed kilns “Round Down Draft Kilns”. 

            Open Bhatta 

            In clamp-burning a foundation consisting of a layer or two of burnt brick is 
            formed as a level site to protect the clamp from damp rising from the ground 
            beneath. Channels are arranged in the foundation in such a way as to form 
            a number of fire holes or flues running the length and breadth of the clamp. 
            These flues are filled with fuel. The green bricks with more fuel between 
            them are stacked and spaced so that the fire can penetrate through the whole 
            mass. The bricks are seen piled in the Figure 3.6. Burnt bricks and mud is 
            laid over the top of the stack to protect it from the weather and heat loss. 
            The clamp is set on fire and allowed to bum. Il can take couple of days. 
            One such arrangement is seen in Figure 3.7. In the ancient period large 
            kilns or clamps must have been used to produce vast number of bricks






            308 



            History of Architecture ami Ancient 
            Building Materials in India Part-II

            required for building the shelter houses for the settlers during the Indus 
            valley civilization. The remains of one such kiln is shown in the Figure 3.8. 
            It was excavated at Lotlial in the Ahemdabad, India and dales back to about 
            2000 B.C. 

            The fuel used is the dry grass, wood, and cakes made out of cow-dung, 
            which are dried and coal. Some of the fuels stocked on the burning site are
            shown in the Figure 3.9. Production of large quantity of bricks requires a 
            large amount of fuel. In case of scarcity of the fuel the bricks were made 
            with the addition of straw which serves as a fuel for burning the bricks. In 
            many cases it was sufficient for burning the bricks or required very little 
            extra fuel. There was an added advantage by mixing straw, the bricks became 
            lighter, as they have created empty space after burning. 


            The temperature attained in the kiln was related to the amount of fuel
            used e.g. number of cakes or the amount of wood etc. The fuel was calculated
            in such a way so that the bricks are properly burnt. There were no 
            thermometers for measuring the temperature. It was estimated by the color 
            of the flame. It was rather accurate. After burning of the fuel, a glow 
            which lasted for a long period as the kiln is covered very tightly with 
            mud. Thus the heat is available for long time which keeps the kiln hot. 
            This is known as soaking period. It means that the temperature remains 
            constant for certain period of time. During this period the sintering process 
            the reaction at high temperature continues. The kiln is opened after few 
            days, When the temperature automatically goes down. Thus the bricks 
            slowly cool down and are not exposed to the sudden temperature change, 
            thermal shock, which will occur if the kiln is opened when still warm. In 
            this situation the bricks will crack due to the unstabilized ceramic bonds 
            and not proper weathering.

            Round Down Draft Kiln 

            More advanced way of burning the bricks was to bum the bricks in a special 
            kiln “Round Down Draft Kiln”. This is used for mass production of the 
            bricks. It is shown photographically in the Figure 3.10. In down draft kiln 
            there are interconnected chambers. The bricks are stacked in these 
            Chambers. The principle is that during burning a draft is created due to the 
            convection currents by the temperature variation. This draft “air” from the 
            burring chamber passes through the outlets to the next chamber and the 
            bricks are preheated. When this chamber goes under heating the burning 
            chamber goes under cooling. Thus the draft passes to the next chamber 
            from the burning chamber all the time. It is a continuous process. Because 






            309 


            of the draft movement, such kilns are named “Down Draft Kilns” This 
            process is productive and saves a lot of energy as it is used in preheating. 

            Tunnel Kiln 

            Now a days the bricks for making the houses in the urban areas are produced 
            in the automatic factories, where the bricks are molded in the brick press, 
            dried and burnt in the tunnel kilns with complete temperature control. The 
            kilns are Fired with furnace oil. The bricks are loaded on the specially made 
            trolley which moves on the rails. These are pushed inside the tunnel kiln. 
            Tne tunnel kiln has three zones; preheating zone, firing zone, and cooling 
            zone. The movement of trolleys is automatically controlled so that they 
            stay in different zones for desired time. The trolleys are pushed out after 
            burning. These are much better in quality; warpage is very low as these are 
            not handled manually, and because of this and the complete control of 
            temperature in the kiln are well burnt and are sound e.g the bricks have less 
            cracks. The rejection is less. The productivity increases and the bricks 
            become cheaper inspite of the expensive Production cost. """)
    )
    kg.create_relationship(section_id, "HAS_SUBSECTION", subsection_id)


    #  now create subsection 3.2.2 Bricks Inspection 
    subsection_id = kg.create_subsection(
        "3.2.2 Bricks Inspection",
        ("""The bricks thus produced are inspected. The inspection is done for the size 
            control “warpage” and the soundness of the bricks e.g. testing of the cracks 
            inside the bricks. Mostly the inspection is done visually or by the sound 
            resonance, which is also performed basing upon the experience of the able 
            builder. The brick is knocked by an iron piece, it produces sound. If the 
            sound produced is not clean and clear the brick has cracks. The warpage is 
            tested completely visually. The bricks, which do not pass these tests, are 
            unfit to be used for building construction and are rejected. 

            These rejected bricks are crushed and used for making the aggregates 
            for making masonry or pulverized for making brick dust known as “ Surkhi ” 
            which is used as a pozzolanic material.""")
    )
    kg.create_relationship(section_id, "HAS_SUBSECTION", subsection_id)

    subsection_id = kg.create_subsection(
        "3.2.3 Brick Size",
        ("""The bricks made were of different sizes. There were small bricks and big 
            bricks, small bricks were called “ Lakhauri ”. These were about three and 
            quarter of an inch thick, and about four by six inches in length and breadth 
            The word Lakhauri itself comes from the word lakh, It means lakh, 
            10 lakh = 1 million) of bricks for construction. There were also larger  and
            heavier bricks about two inches thick, which were known as Pan Patta 
            according to P.C. Mukherji or "Ilmasi" after Ilmas Ali Khan, the Deputy 
            Governor of Oudh during the time of Saadat Ali Khan, who reportedly used
            these thicker bricks in his own buildings. There are also instances where 
            curved bricks and triangular bricks were made. The tr iangular bricks were 
            used for making the core of the statues. However there was no specific 
            standard about the size. Smaller bricks, lakhauri owing to the great number 
            used gave tremendous strength to the structure. The other advantage is that 
            the* can be used both with the “Pan Patta” bricks and also by themselves to 
            form remarkably fine details even before the stucco has been applied. 
            Similarly, the big bricks because of the bigger size work as load bearing 
            blocks. Some of the bricks are shown in the Figures 3.11 and 3.12.""")
    )
    kg.create_relationship(section_id, "HAS_SUBSECTION", subsection_id)


    
    # 7. (Optional) Create a Reference node for a citation and link it to the Section
    reference1_id = kg.create_reference(
        "Craven, R.C.",
        "1. Craven, R.C., [1979], A Concise History of Indian Art, Vikas Publishing House, New Delhi, 13. "
    )
    kg.create_relationship(section_id, "CITES", reference1_id)

    reference2_id = kg.create_reference(
        "Joshi, J.P. and Bisht, R.S. [1994]",
        "2. Joshi, J.P. and Bisht, R.S. [1994], India and the Indus civilization, Archaeological Survey of India, National Museum Instate (Deemed University), New Delhi, India.  "
    )
    kg.create_relationship(section_id, "CITES", reference2_id)

    reference3_id = kg.create_reference(
        "Verma, U. [ 1996]",
        "4. Verma, U. [ 1996], Delhi in the magnificent neighbor- Indraprastha, India Prospective July 1996."
    )
    kg.create_relationship(section_id, "CITES", reference3_id)
