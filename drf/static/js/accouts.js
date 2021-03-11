    function initialUserTable (){
      $('#user-table') .bootstrapTable({                        
          url: "/accounts/api/user/",
        showColumns : true,
        showColumnsToggleAll:true, //�b����ܶ}�Ҷ}���������
        showToggle : true, //�W����/table������
        showPaginationSwitch : true, //����/����������
        showRefresh : true, //���s��z
        showFullscreen: true,
        search : true, //�d�� 
        pagination : true, 
        pageSize : 15,    
        height:500,
        buttons :"buttons",
        toolbar :"#toolbar",
        uniqueId :"id",
        columns: [ 
              {               
                title:'State',
                checkbox:true,                               
              },
              { 
                field :"id",
                title:'ID',
                visible:false, 
              },
              { 
                field :"username",
                title:'User Name',                             
              },
              { 
                field :"first_name", 
                title:'First Name',                                                    
              },      
              { 
                field :"last_name", 
                title:'Last Name',                                                    
              },      
              { 
                field :"email", 
                title:'Email',                                                    
              },   
              { 
                field :"profile.cell_phone_number", 
                title:'Cell Phone',                                                    
              }, 
              { 
                field :"profile.points", 
                title:'Points',                                                    
              },                 
          ],

        })                      

    }







