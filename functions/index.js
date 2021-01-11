const functions = require('firebase-functions');
const admin = require('firebase-admin');
admin.initializeApp();

// // Create and Deploy Your First Cloud Functions
// // https://firebase.google.com/docs/functions/write-firebase-functions
//
// exports.helloWorld = functions.https.onRequest((request, response) => {
//   functions.logger.info("Hello logs!", {structuredData: true});
//   response.send("Hello from Firebase!");
// });

/*await admin.database().ref('games/').limitToLast(1).once('value', snap => {
		
		snap.forEach((childSnapshot) => {
			var value = childSnapshot.val();
			console.log(value);
			gameId=value.id;
			console.log(value.id);
		}
});*/



exports.addPoint = functions.database.ref('games/{gameId}/points/{pointId}').onCreate( async (snapshot, context) => {
	
			var point = snapshot.val();

			
										
	
					
					console.log(point);
					
					console.log("adding point")
					if(point){
						console.log(point.id);
						if (point.type <1){
							admin.database().ref('users/' + point.id).update({points: admin.database.ServerValue.increment(1)});
						}
						else{
							admin.database().ref('users/' + point.id).update({plunks: admin.database.ServerValue.increment(1)});
							admin.database().ref('users/' + point.id).update({points: admin.database.ServerValue.increment(1)});
						}
						
						var game = await admin.database().ref('/games/' + context.params.gameId).once('value');
							
						
						
						if(point.id === game.val().player1 || point.id === game.val().player2){
							admin.database().ref('games/' + context.params.gameId).update({t1Score: admin.database.ServerValue.increment(1)});
						}
						else{
							admin.database().ref('games/' + context.params.gameId).update({t2Score: admin.database.ServerValue.increment(1)});
						}
					}
					
		

									
				
			
		
		
		
		
		
});
    

							
		
	
