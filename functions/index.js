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

exports.addPoint = functions.database.ref('games/').onCreate( async(snapshot, context) => {
	
	await admin.database().ref('games/').limitToLast(1).once('value', snap => {
		
		snap.forEach((childSnapshot) => {

			var value = childSnapshot.val();
			console.log(value);
			gameId=value.id;
			console.log(value.id);
			if (value.isActive){
				console.log("active");
				admin.database().ref('games/' + gameId+"/points/").limitToLast(1).on('child_added', newSnap => {
										
	
					point =newSnap.val();
					console.log(point);
					console.log("adding point")
					admin.database().ref('users/' + point.id).update({points: admin.database.ServerValue.increment(1)});
					
					if(point.id === value.player1 || point.id === value.player2){
						admin.database().ref('games/' + gameId).update({t1Score: admin.database.ServerValue.increment(1)});
					}
					else{
						admin.database().ref('games/' + gameId).update({t2Score: admin.database.ServerValue.increment(1)});
					}
					console.log(point.id);
		

									
				});
			}
		
		});
		
		
		
	});
    

							
		
	
});